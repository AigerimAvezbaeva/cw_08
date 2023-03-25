from django.db import models
from django.db.models import TextChoices


class CategoryChoice(TextChoices):
    CLEANING = 'Cleaning', 'Уборка'
    REPAIR = 'Repair', 'Ремонт'
    COPYWRITING = 'Copywriting', 'Копирайтинг'
    FOOD = 'Food', 'Еда'
    COOKING = 'Cooking', 'Готовка'
    DELIVERY = 'Delivery', 'Доставка'
    OTHER = 'Other', 'Другое'


class Product(models.Model):
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Название'
    )
    category = models.CharField(
        verbose_name='Категория',
        max_length=50,
        choices=CategoryChoice.choices,
        default=CategoryChoice.OTHER
    )
    description = models.TextField(
        max_length=3000,
        null=False,
        blank=False,
        verbose_name="Описание"
    )
    image = models.ImageField(
        verbose_name='Фото продукта',
        null=True,
        blank=True,
        upload_to='avatars'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
