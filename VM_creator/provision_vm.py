from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient
from .connection import WebSocket
import os
from dotenv import load_dotenv


async def provision_vm(socket: WebSocket):
    dotend_path = os.path.join(os.getcwd(), ".env")
    load_dotenv(dotend_path)

    await socket.accept()
    message = await socket.receive_text()
    vm_name, resource_group_name, configuration_name = message.split(",")
    credential = AzureCliCredential()

    subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]

    resource_client = ResourceManagementClient(credential, subscription_id)

    RESOURCE_GROUP_NAME = resource_group_name
    LOCATION = "centralus"

    rg_result = resource_client.resource_groups.create_or_update(
        RESOURCE_GROUP_NAME, {"location": LOCATION}
    )

    await socket.send_text(
        f"Создан пул ресурсов {rg_result.name} в {rg_result.location} локации"
    )

    VNET_NAME = f"{vm_name}-vnet"
    SUBNET_NAME = f"{vm_name}-subnet"
    IP_NAME = f"{vm_name}-ip"
    IP_CONFIG_NAME = f"{vm_name}-config"
    NIC_NAME = f"{vm_name}-nic"

    network_client = NetworkManagementClient(credential, subscription_id)

    poller = network_client.virtual_networks.begin_create_or_update(
        RESOURCE_GROUP_NAME,
        VNET_NAME,
        {
            "location": LOCATION,
            "address_space": {"address_prefixes": ["10.0.0.0/16"]},
        },
    )

    vnet_result = poller.result()

    await socket.send_text(
        f"Создана виртуальная сеть {vnet_result.name} с префиксом {vnet_result.address_space.address_prefixes}"
    )

    poller = network_client.subnets.begin_create_or_update(
        RESOURCE_GROUP_NAME,
        VNET_NAME,
        SUBNET_NAME,
        {"address_prefix": "10.0.0.0/24"},
    )
    subnet_result = poller.result()

    await socket.send_text(
        f"Создана виртуальная подсеть {subnet_result.name} с префиксом {subnet_result.address_prefix}"
    )

    poller = network_client.public_ip_addresses.begin_create_or_update(
        RESOURCE_GROUP_NAME,
        IP_NAME,
        {
            "location": LOCATION,
            "sku": {"name": "Standard"},
            "public_ip_allocation_method": "Static",
            "public_ip_address_version": "IPV4",
        },
    )

    ip_address_result = poller.result()

    await socket.send_text(
        f"Создан публичный IP адресс {ip_address_result.name} с аддрессом {ip_address_result.ip_address}"
    )

    poller = network_client.network_interfaces.begin_create_or_update(
        RESOURCE_GROUP_NAME,
        NIC_NAME,
        {
            "location": LOCATION,
            "ip_configurations": [
                {
                    "name": IP_CONFIG_NAME,
                    "subnet": {"id": subnet_result.id},
                    "public_ip_address": {"id": ip_address_result.id},
                }
            ],
        },
    )

    nic_result = poller.result()

    await socket.send_text(f"Создан сетевой интерфейс {nic_result.name}")

    compute_client = ComputeManagementClient(credential, subscription_id)

    VM_NAME = vm_name
    USERNAME = os.environ.get("POSTGRES_USER")
    PASSWORD = os.environ.get("POSTGRES_PASSWORD")

    await socket.send_text(
        f"Создаём виртуальную машину {VM_NAME}; это займёт какое-то время."
    )

    poller = compute_client.virtual_machines.begin_create_or_update(
        RESOURCE_GROUP_NAME,
        VM_NAME,
        {
            "location": LOCATION,
            "storage_profile": {
                "image_reference": {
                    "publisher": "Canonical",
                    "offer": "UbuntuServer",
                    "sku": "16.04.0-LTS",
                    "version": "latest",
                }
            },
            "hardware_profile": {"vm_size": configuration_name},
            "os_profile": {
                "computer_name": VM_NAME,
                "admin_username": USERNAME,
                "admin_password": PASSWORD,
            },
            "network_profile": {
                "network_interfaces": [
                    {
                        "id": nic_result.id,
                    }
                ]
            },
        },
    )

    vm_result = poller.result()

    await socket.send_text(f"Создана виртуальная машина {vm_result.name}")
    await socket.close()
