"""
URL configuration for django_crud_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from backend_api.views import all_products
from backend_api.views import wood_list
from backend_api.views import lighting_list
from backend_api.views import appliance_list
from backend_api.views import paint_list
from backend_api.views import landscaping_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('all-products/', all_products, name='all-products'),
    path('appliances/', appliance_list, name='appliance-list'),
    path('lightings/', lighting_list, name='lighting-list'),
    path('woods/', wood_list, name='wood-list'),
    path('landscapings/', landscaping_list, name='landscaping-list'),
    path('paints/', paint_list, name='paint-list'),
]