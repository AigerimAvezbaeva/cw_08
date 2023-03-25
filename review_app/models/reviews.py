from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from review_app.managers import ReviewManager


class Review(models.Model):
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        verbose_name='Автор отзыва',
        related_name='review_author',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        to='review_app.Product',
        verbose_name='Продукт с отзывом',
        related_name='reviewed_product',
        on_delete=models.CASCADE
    )
    review = models.CharField(
        max_length=1000,
        null=False,
        blank=False,
        verbose_name='Отзыв'
    )
    rating = models.IntegerField(
        verbose_name='Оценка',
        null=False,
        blank=False,
        validators=[
            MaxValueValidator(limit_value=5, message='Значение не может быть более 5'),
            MinValueValidator(limit_value=1, message='Значение не может быть менее 1')
        ]
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    objects = ReviewManager()
