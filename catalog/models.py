import re
from decimal import Decimal
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

# Գույնի ստուգման ֆունկցիա (վավեր HEX կոդ կամ հիմնական գույների անուններ)
def validate_color_format(value):
    val_clean = value.strip()
    hex_regex = r'^#(?:[0-9a-fA-F]{3}){1,2}$'
    allowed_names = [
        'black', 'white', 'brown', 'beige', 'grey', 'gray', 
        'blue', 'green', 'wood', 'red', 'cream', 'natural'
    ]
    
    if not (re.match(hex_regex, val_clean) or val_clean.lower() in allowed_names):
        raise ValidationError(
            "Գույնը պետք է լինի վավեր HEX կոդ (օր.՝ #FFFFFF կամ #8B4513) կամ գույնի անուն (օր.՝ Brown, Black, White):"
        )


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Կատեգորիայի անունը")
    slug = models.SlugField(unique=True, verbose_name="Հղում (Slug)")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Կատեգորիա"
        verbose_name_plural = "Կատեգորիաներ"


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Ապրանքի անունը")
    
    # Category դառնում է առանձին աղյուսակի հղում
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name='products', 
        verbose_name="Կատեգորիա"
    )
    
    # Գնի ստուգում՝ նվազագույնը 0.01 (բացասական կամ 0 չի կարող լինել)
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(Decimal('0.01'), message="Գինը պետք է լինի մեծ 0-ից:")],
        verbose_name="Գինը"
    )
    
    image = models.ImageField(upload_to="products/", verbose_name="Նկար")
    short_description = models.CharField(max_length=255, verbose_name="Կարճ նկարագրություն")
    description = models.TextField(verbose_name="Ամբողջական նկարագրություն")
    material = models.CharField(max_length=100, verbose_name="Նյութ")
    
    # Գույնի ստուգում
    color = models.CharField(
        max_length=50, 
        validators=[validate_color_format],
        verbose_name="Գույն (HEX կոդով)"
    )
    
    in_stock = models.BooleanField(default=True, verbose_name="Առկա է")
    slug = models.SlugField(unique=True, verbose_name="Հղում (Slug)")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ապրանք"
        verbose_name_plural = "Ապրանքներ"