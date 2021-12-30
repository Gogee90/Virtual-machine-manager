from django.urls import path

# from websocket.urls import websocket
from . import views
from .provision_vm import provision_vm

urlpatterns = [
    path("", views.ListVirtualMachines.as_view(), name="virtual-machines-list"),
    path(
        "create/",
        views.VirtualMachineCreate.as_view(),
        name="virtual-machine-create",
    ),
    path(
        "edit/<int:pk>",
        views.UpdateVirtualMachine.as_view(),
        name="virtual-machine-edit",
    ),
    path(
        "delete/<int:pk>",
        views.delete_virtual_machine,
        name="virtual-machine-delete",
    ),
    path(
        "get-configuration/<int:pk>", views.get_configuration, name="get-configuration"
    ),
    path("ws/", provision_vm),
]
