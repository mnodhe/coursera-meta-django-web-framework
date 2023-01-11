from django.contrib import admin
from .models import Logger, Menu
from .models import MenuCategory
from .models import Customer
# Register your models here.

admin.site.register(Menu)
admin.site.register(MenuCategory)
admin.site.register(Customer)
admin.site.register(Logger)
