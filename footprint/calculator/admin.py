from django.contrib import admin
from .models import OfficeOperationForm, EmissionFactor
# Register your models here.



admin.site.site_header = "PZE Admin"
admin.site.site_title = "PZE Admin"
admin.site.index_title = "Welcome to PZE Admin"

admin.site.register(OfficeOperationForm)
admin.site.register(EmissionFactor)