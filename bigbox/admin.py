from django.contrib import admin
from bigbox.models import Box, Category, Activity, Reason

# Register your models here.


@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'purchase_available']
    list_display_links = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'slug', 'order']
    list_display_links = ['name']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'purchase_available']
    list_display_links = ['name']


@admin.register(Reason)
class ReasonAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'order']
    list_display_links = ['name']
