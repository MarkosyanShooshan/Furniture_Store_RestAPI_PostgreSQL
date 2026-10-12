from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'catalog'


# Այստեղ օգտագործում ենք DRF-ի DefaultRouter-ը, որն ավտոմատ գեներացնում է API-ի բոլոր անհրաժեշտ URL-ները (GET, POST, PUT, DELETE):
# Ստեղծում ենք Router API-ի համար
router = DefaultRouter()
router.register(r'api/categories', views.CategoryViewSet)
router.register(r'api/products', views.ProductViewSet)


urlpatterns = [
    # HTML էջերի URL-ները
    path('', views.product_list, name='product_list'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),

    # REST API-ի URL-ները
    path('', include(router.urls)),
]