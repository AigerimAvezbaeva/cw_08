from django.urls import path

from review_app.views.products import ProductsView, ProductView, AddProductView, ProductUpdateView, ProductDeleteView, \
    ProductAddReviewView
from review_app.views.reviews import ReviewUpdateView, ReviewDeleteView

urlpatterns =[
    path('', ProductsView.as_view(), name='index'),
    path('product/<int:pk>', ProductView.as_view(), name='product_detail'),
    path('products/add/', AddProductView.as_view(), name='add_product'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='edit_product'),
    path('products/<pk>/delete/', ProductDeleteView.as_view(), name='delete_product'),

    path('products/<int:pk>/reviews/add/', ProductAddReviewView.as_view(), name='add_review'),
    path('products/<int:ppk>/reviews/<int:pk>/edit/', ReviewUpdateView.as_view(), name='edit_review'),
    path('products/<int:ppk>/reviews/<int:pk>/delete/', ReviewDeleteView.as_view(), name='delete_review'),
    path('products/<int:ppk>/reviews/<int:pk>/delete/confirm-delete-review/', ReviewDeleteView.as_view(),
         name='confirm_delete_review'),
]
