from .models import VirtualMachine
from .widgets import RangeInput
from django import forms


class VirtualMachineForm(forms.ModelForm):
    ram_capacity = forms.IntegerField(widget=RangeInput, min_value=1, max_value=12000)
    cpu_cores = forms.IntegerField(widget=RangeInput, min_value=1, max_value=416)
    hdd_capacity = forms.IntegerField(widget=RangeInput, min_value=10, max_value=1024)

    class Meta:
        model = VirtualMachine
        fields = "__all__"
