# Create your models here.
from django.db import models


class CommonInfo(models.Model):
    name = models.CharField(max_length=200, verbose_name='nombre')
    slug = models.SlugField()
    order = models.IntegerField(verbose_name=u'orden', default=0)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Reason(CommonInfo):
    pass


class Category(CommonInfo):
    description = models.TextField(verbose_name=u'descripción')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=200)
    internal_name = models.CharField(max_length=200)
    description = models.TextField(verbose_name=u'descripción')
    category = models.ForeignKey(
        Category, verbose_name='categoría', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        verbose_name_plural = "Products"


class Activity(Product):
    reasons = models.ManyToManyField(Reason, verbose_name='tags', blank=True)
    purchase_available = models.BooleanField(
        verbose_name='disponible venta individual', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Activities"


class Box(Product):
    activities = models.ManyToManyField(Activity)
    price = models.IntegerField(verbose_name='precio de venta')
    purchase_available = models.BooleanField(
        verbose_name='disponible venta individual', default=False)
    slug = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Boxes"
