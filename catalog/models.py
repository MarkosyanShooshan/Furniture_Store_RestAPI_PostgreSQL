from django.db import models



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
    # Այստեղ Category դառնում է առանձին աղյուսակի հղում
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Կատեգորիա")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Գինը")
    image = models.ImageField(upload_to="products/", verbose_name="Նկար") 
    short_description = models.CharField(max_length=255, verbose_name="Կարճ նկարագրություն")
    description = models.TextField(verbose_name="Ամբողջական նկարագրություն")
    material = models.CharField(max_length=100, verbose_name="Նյութ")
    color = models.CharField(max_length=50, verbose_name="Գույն (HEX կոդով)")
    in_stock = models.BooleanField(default=True, verbose_name="Առկա է")
    slug = models.SlugField(unique=True, verbose_name="Հղում (Slug)")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ապրանք"
        verbose_name_plural = "Ապրանքներ"