from django.contrib import admin
from review_app.models import Product, Review


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ('title', 'category')
    search_fields = ('title', 'category')
    fields = ('id', 'title', 'category', 'description', 'image')
    readonly_fields = ('id',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'product', 'rating')
    list_filter = ('author', 'product')
    search_fields = ('author', 'product')
    fields = ('id', 'author', 'product', 'review', 'rating')
    readonly_fields = ('id',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)

