from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description')


admin.site.register(Category, CategoryAdmin)
