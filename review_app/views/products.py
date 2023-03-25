from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Avg
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from review_app.forms.products import ProductForm
from review_app.forms.reviews import ReviewForm
from review_app.models import Product, Review


class GroupPermission(UserPassesTestMixin):
    groups = []

    def test_func(self):
        return self.request.user.groups.filter(name__in=self.groups).exists()


class SuccessDetailUrlMixin:
    def get_success_url(self):
        return reverse('index', kwargs={'pk': self.object.pk})


class AddProductView(GroupPermission, SuccessDetailUrlMixin, LoginRequiredMixin, CreateView):
    template_name = 'add_product.html'
    form_class = ProductForm
    model = Product
    extra_context = ()
    groups = ('Moderators', 'admin')

    def form_valid(self, form):
        form = self.form_class(self.request.POST, self.request.FILES)
        form.save()
        return super().form_valid(form)


class ProductsView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'
    queryset = Product.objects.all()
    paginate_by = 4
    paginate_orphans = 0


class ProductView(DetailView):
    template_name = 'product_detail.html'
    model = Product


class ProductUpdateView(GroupPermission, SuccessDetailUrlMixin, LoginRequiredMixin, UpdateView):
    template_name = 'edit_product.html'
    form_class = ProductForm
    model = Product
    groups = ('Moderators', 'admin')


class ProductDeleteView(GroupPermission, DeleteView, LoginRequiredMixin):
    template_name = 'delete_product.html'
    model = Product
    success_url = reverse_lazy('index')
    groups = ('Moderators', 'admin')


class ProductAddReviewView(GroupPermission, LoginRequiredMixin, CreateView):
    template_name = 'add_review.html'
    form_class = ReviewForm
    model = Product
    extra_context = ()
    groups = ('Moderators', 'admin')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            product = self.get_object()
            print(product.title)
            review = form.save(commit=False)
            review.product = product
            review.author = request.user
            review.save()
            return redirect('products_list', product.pk)
        context = {}
        context['form'] = form
        return self.render_to_response(context)
