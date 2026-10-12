from django.shortcuts import render,get_object_or_404


from rest_framework import viewsets
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer




# --- HTML Views (Կայքէջի HTML էջերի համար) ---
def product_list(request):
    products = Product.objects.all()
    # կամ products = Product.objects.select_related('category').all()
    return render(request, "catalog/index.html", {"products": products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "catalog/furniture-details.html", {"product": product})

# Այստեղ ավելացնում ենք ViewSet-ներ API-ի համար՝ պահպանելով նաև HTML էջերի համար նախատեսված views-ը։
# --- REST API ViewSets (JSON տվյալներ վերադարձնելու համար) ---
class CategoryViewSet(viewsets.ModelViewSet):
   
    # API endpoint կատեգորիաների դիտման և խմբագրման համար:
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
   
    # API endpoint ապրանքների դիտման և խմբագրման համար:
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'  # Ապրանքները slug-ով ստանալու համար (օր. /api/products/olivia-velvet-sofa/)