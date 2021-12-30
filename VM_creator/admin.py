from django.contrib import admin
from .models import Configurations, Division, Pool, VirtualMachine

# Register your models here.
admin.site.register(Division)
admin.site.register(Pool)
admin.site.register(VirtualMachine)
admin.site.register(Configurations)
