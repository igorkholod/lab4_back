from django.contrib import admin
from .models import Description, Drug, Pharmacy, Manufacturer, DrugPharmacy

# Register your models here.
admin.site.register(Description)
admin.site.register(Drug)
admin.site.register(Pharmacy)
admin.site.register(Manufacturer)
admin.site.register(DrugPharmacy)
