from django.contrib import admin
from django import forms
from django.utils.html import format_html
from .models import Status, Type, Category, Subcategory, CashFlow

class SubcategoryInline(admin.TabularInline):
    model = Subcategory
    extra = 1
    fields = ('name', )

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name',)
    list_per_page = 20

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    list_per_page = 20

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'subcategories_count')
    search_fields = ('name', )
    list_per_page = 20
    inlines = [SubcategoryInline]

    def subcategories_count(self, obj):
        count = obj.subcategories.count()
        return format_html(
            '<a href="{}?category__id__exact={}">{}</a>',
            f'/admin/server/subcategory/',
            obj.id,
            f"{count} подкатегорий"
        )
    subcategories_count.short_description = 'Подкатегории'

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'category__name')
    list_per_page = 20

@admin.register(CashFlow)
class CashFlowAdmin(admin.ModelAdmin):
    list_display = ('date', 'status', 'type', 'category', 'subcategory', 'amount', 'comment')
    list_filter = ('date', 'status', 'type', 'category', 'subcategory')
    search_fields = ('comment', 'category__name', 'subcategory__name')
    date_hierarchy = 'date'
    list_per_page = 20
    ordering = ('-date', '-created_at')
