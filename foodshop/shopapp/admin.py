from django.contrib import admin
from shopapp.models import fooditem

# Register your models here.
class itemadmin(admin.ModelAdmin):
    list_display=['id','name','price','fdetails','cat','is_active']
    list_filter=['price','cat','is_active']



admin.site.register(fooditem,itemadmin) 