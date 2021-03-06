"""FPPlite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from FPP.views import CreateCategoryView, EditCategoryView, ContractorsCreate, EditContractorView, ProductCreatorView, \
    EditProductCreatorView, LandingPageView, WarehouseView, SaleView, DeliveryView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view()),
    path('category/', CreateCategoryView.as_view()),
    path('category/<int:id>', EditCategoryView.as_view()),
    path('addproduct/', ProductCreatorView.as_view()),
    path('warehouse/', WarehouseView.as_view()),
    path('products/<int:id>', EditProductCreatorView.as_view()),
    path('sale/', SaleView.as_view()),
    # path('sale/<int:id>'),                      # szczegoły dostawy
    path('delivery/', DeliveryView.as_view()),
    # path('delivery/<int:id>'),                  # szczegóły dostawy
    path('contractors/', ContractorsCreate.as_view()),
    path('contractor/<int:id>', EditContractorView.as_view())

]
