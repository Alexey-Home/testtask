from django.contrib import admin

from django.contrib import admin

from .models import *


class LessonsAdmin(admin.ModelAdmin):
    list_display = ("title", 'link', "duration", "get_products")

class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "get_products")

class LessonsInline(admin.TabularInline):
    model = Lessons.products.through

class ProfileInline(admin.TabularInline):
    model = Profile.products.through

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    model = Products
    inlines = [
        LessonsInline,
    ]

admin.site.register(Lessons, LessonsAdmin)
admin.site.register(Profile, ProfileAdmin)

