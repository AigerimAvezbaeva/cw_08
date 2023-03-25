from django import forms

from review_app.models import Review, Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'category', 'description', 'image')
        labels = {
            'title': 'Название',
            'category': 'Категория',
            'description': 'Описание',
            'image': 'Фото'
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('review', 'rating')
        labels = {
            'review': 'Отзыв',
            'rating': 'Оценка'
        }
