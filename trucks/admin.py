from django.contrib import admin
from trucks.models import Truck,Trailer,WheelTruck,WheelTrailer
# Register your models here.

class TruckAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['plate_number','comments','trailer']}),
        ('Dates', {'fields': ['maintenance_date']}),
    ]

class TrailerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['plate_number','comments']}),
        ('Dates', {'fields': ['maintenance_date']}),
    ]

admin.site.register(Truck,TruckAdmin)
admin.site.register(Trailer,TrailerAdmin)
admin.site.register(WheelTruck)
admin.site.register(WheelTrailer)

