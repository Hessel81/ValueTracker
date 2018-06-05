from django.contrib import admin
from .models import WeightData

   
class WeightDataAdmin(admin.ModelAdmin):   
    list_display = ( 'check_date', 'weight_value' )
    list_filter = ['check_date']
    date_hierarchy = 'check_date'
   
admin.site.register(WeightData, WeightDataAdmin)
