from django.contrib import admin

# Register your models here.
from .models import *

class MenuAdmin(admin.ModelAdmin):
    list_display = ['id','RestaurantName','ItemName','price']
    filter = ['RestaurantName','ItemName']


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['id','RestaurantNmame','phoneno','address']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['username','restaurant','itemname','price','phoneno','address']
    

admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Menu,MenuAdmin)
admin.site.register(Order,OrderAdmin)
