from django.urls import path
from . import views

app_name = 'basic'

urlpatterns = [
    path('', views.homeView, name='home'),
    path('<int:id>/', views.product_detail, name='detail'),
    path('<slug:category_slug>/', views.categoryView, name='category_view'),
]
