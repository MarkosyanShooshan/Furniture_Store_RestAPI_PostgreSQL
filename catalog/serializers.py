import re
from decimal import Decimal
from rest_framework import serializers
from .models import Category, Product

# Serializer-ները Python-ի մոդելների տվյալները վերածում են JSON ֆորմատի

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'slug',
            'category',
            'category_name',
            'price',
            'image',
            'short_description',
            'description',
            'material',
            'color',
            'in_stock',
        ]

    # Գնի ստուգում API-ում
    def validate_price(self, value):
        if value <= Decimal('0.00'):
            raise serializers.ValidationError("Գինը չի կարող լինել բացասական կամ 0:")
        return value

    # Գույնի ստուգում API-ում
    def validate_color(self, value):
        val_clean = value.strip()
        hex_regex = r'^#(?:[0-9a-fA-F]{3}){1,2}$'
        allowed_names = [
            'black', 'white', 'brown', 'beige', 'grey', 'gray', 
            'blue', 'green', 'wood', 'red', 'cream', 'natural'
        ]
        
        if not (re.match(hex_regex, val_clean) or val_clean.lower() in allowed_names):
            raise serializers.ValidationError(
                f"«{value}» գույնն անթույլատրելի է: Ուղարկեք վավեր HEX կոդ (օր.՝ #FFFFFF կամ #8B4513) կամ գույնի անուն (օր.՝ Brown, Black, White):"
            )
        return val_clean