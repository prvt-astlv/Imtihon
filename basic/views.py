from django.shortcuts import render, get_object_or_404
from .models import *
from django.views import generic
from cart.forms import CartAddProductForm


# Create your views here.
class HomeView(generic.ListView):
    model = Product
    template_name = 'basic/home.html'
    context_object_name = 'products'
    # extra_context = 'categories'


class DetailView(generic.DetailView):
    model = Product
    template_name = 'basic/detail.html'
    context_object_name = 'product'


# function based views
def product_detail(request, id):
    product = Product.objects.get(id=id)
    cart_product_form = CartAddProductForm()
    return render(request, 'basic/detail.html', {'product': product, 'cart_product_form': cart_product_form})

def categoryView(request, category_slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'basic/by_category.html', {'category': category,
                                                      'categories': categories,
                                                      'products': products})

def homeView(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, template_name='basic/home.html', context=context)
