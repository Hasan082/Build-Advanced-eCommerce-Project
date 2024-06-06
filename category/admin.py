from django.contrib import admin
from .models import Category


# Defining the CategoryAdmin class to customize the admin interface for the Category model.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    # list_display specifies the fields to display in the list view of the Category model.
    list_display = ('name', 'slug', 'description')


# Registering the Category model with the admin site using the CategoryAdmin class.
admin.site.register(Category, CategoryAdmin)
