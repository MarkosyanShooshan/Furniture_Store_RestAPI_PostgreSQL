
from django.contrib import admin
from django.forms import TextInput
from .models import Product, Category



# Գրանցում ենք կատեգորիան
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "in_stock", "color")
    list_filter = ("category", "in_stock", "color")
    search_fields = ("name", "category__name") # որոնում ենք ըստ կատեգորիայի անվան
    prepopulated_fields = {"slug": ("name",)}
    list_per_page = 20
    
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'color':
            kwargs['widget'] = TextInput(attrs={'type': 'color', 'style': 'height: 30px; width: 50px; padding: 0;'})
        return super().formfield_for_dbfield(db_field, request, **kwargs)