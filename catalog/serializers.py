from rest_framework import serializers
from .models import Category, Product




# Serializer-ները Python-ի մոդելների տվյալները վերածում են JSON ֆորմատի, որպեսզի REST API-ն կարողանա դրանք ուղարկել։

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class ProductSerializer(serializers.ModelSerializer):
    # Category-ի անունը JSON-ում ցույց տալու համար
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