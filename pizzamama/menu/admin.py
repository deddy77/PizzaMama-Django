from django.contrib import admin
from .models import Pizza


class PizzaAdmin(admin.ModelAdmin):
    list_display = ("name", "ingredients", "price", "vegetarian")
    search_fields = ["name"]
admin.site.register(Pizza, PizzaAdmin)

# Register your models here.
