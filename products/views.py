from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.core.exceptions import ObjectDoesNotExist

from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSet, SearchableListMixin

from .forms import CategoryForm, ProductForm
from .models import Category, Uom, Product


class ProductHomeView(TemplateView):
    template_name = "products/home.html"


class CategoryListView(ListView):
    model = Category

class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()
        context["product_list"] = category.product_set.all()
        return context

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm


class UomListView(ListView):
    model = Uom

class UomDetailView(DetailView):
    model = Uom

class UomCreateView(CreateView):
    model = Uom
    template_name = "base_form.html"

class UomUpdateView(UpdateView):
    model = Uom
    template_name = "base_form.html"


class ProductListView(SearchableListMixin, ListView):
    model = Product
    paginate_by = 50
    search_fields = ["model", "description"]

class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context["pricelistentry_list"] = product.pricelistentry_set.all()
        return context

class ProductCreateView(CreateWithInlinesView):
    model = Product
    form_class = ProductForm

class ProductUpdateView(UpdateWithInlinesView):
    model = Product
    form_class = ProductForm
