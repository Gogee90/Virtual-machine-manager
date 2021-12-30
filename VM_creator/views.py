from django.http.response import Http404, JsonResponse
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from .forms import VirtualMachineForm
from .models import Configurations, VirtualMachine


# Create your views here.
class ListVirtualMachines(ListView):
    model = VirtualMachine


class VirtualMachineCreate(CreateView):
    template_name = "VM_creator/create_update_form.html"
    form_class = VirtualMachineForm
    success_url = "/"


class UpdateVirtualMachine(UpdateView):
    template_name = "VM_creator/create_update_form.html"
    model = VirtualMachine
    form_class = VirtualMachineForm
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_created"] = True
        return context


def delete_virtual_machine(request, pk):
    try:
        VirtualMachine.objects.get(pk=pk).delete()
        return redirect("/")
    except Exception as e:
        raise Http404


def get_configuration(request, pk):
    try:
        config = Configurations.objects.get(pk=pk)
        vm = dict()
        vm["name"] = config.name
        vm["number_of_cores"] = config.number_of_cores
        vm["os_disk_space"] = config.os_disk_space
        vm["hdd_capacity"] = config.resource_disk_size_in_mb
        vm["ram_capacity"] = config.memory_in_mb
        vm["max_data_disk_count"] = config.max_data_disk_count
        return JsonResponse({"config": vm})
    except Exception as e:
        raise Http404
