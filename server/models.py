from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

class Status(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

class Type(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    type = models.ForeignKey(Type, on_delete=models.PROTECT, related_name='categories')

    def __str__(self):
        return f"{self.name} ({self.type.name})"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        unique_together = ['name', 'type']

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
        unique_together = ['name', 'category']

class CashFlow(models.Model):
    date = models.DateField(default=timezone.now)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.date} - {self.type.name} - {self.amount}"

    class Meta:
        verbose_name = 'Движение денежных средств'
        verbose_name_plural = 'Движения денежных средств'
        ordering = ['-date', '-created_at'] 