from django.shortcuts import render
from django.views import View
from FPP.forms import CategoryForm, ContractorForm, ProductsForm, EditProductsForm
from django.http import HttpResponseRedirect
from FPP.models import Category, Contractor, Product, ProductHistory


class LandingPageView(View):
    def get(self, request):
        return render(request, "landing_page.html")

class CreateCategoryView(View):
    def get(self, request):
        category = Category.objects.all()
        form = CategoryForm()
        return render(request, "category.html", {"form":form,
                                                 "category":category})

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/category")
        else:
            return render(request, "category.html", {"form": form})


class EditCategoryView(View):
    def get(self, request, id):
        form = CategoryForm()
        return render(request, "edit_category.html", {"form":form})

    def post(self,request, id):
        form = CategoryForm(request.POST)
        if form.is_valid():
            cat = Category.objects.get(pk=id)
            cat.category = form.cleaned_data['category']
            cat.save()
            return HttpResponseRedirect("/category")
        else:
            return render(request, "edit_category.html", {"form": form})


class ContractorsCreate(View):
    def get(self, request):
        contractors = Contractor.objects.order_by('name')
        form = ContractorForm()
        return render(request, "contractors.html", {"form":form,
                                                    "contractors":contractors})

    def post(self, request):
        contractors = Contractor.objects.order_by('name')
        form = ContractorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/contractors")
        else:
            return render(request, "contractors.html", {"form": form,
                                                        "contractors": contractors})


class EditContractorView(View):
    def get(self, request, id):
        form = ContractorForm()
        return render(request, "edit_contractor.html", {"form":form})

    def post(self,request, id):
        form = ContractorForm(request.POST)
        if form.is_valid():
            cont = Contractor.objects.get(pk=id)
            cont.name = form.cleaned_data['name']
            cont.contact = form.cleaned_data['contact']
            cont.debt = form.cleaned_data['debt']
            cont.type = form.cleaned_data['type']
            cont.save()
            return HttpResponseRedirect("/contractors")
        else:
            return render(request, "edit_contractor.html", {"form": form})


class ProductCreatorView(View):
    def get(self, request):
        products = Product.objects.order_by('code')
        form = ProductsForm()
        return render(request, "warehouse.html", {"form":form,
                                                    "products":products})

    def post(self, request):
        products = Product.objects.all()
        form = ProductsForm(request.POST)
        if form.is_valid():
            new_product = Product.objects.create(code=form.cleaned_data['code'],
                                                 name=form.cleaned_data['name'],
                                                 quantity=form.cleaned_data['quantity'],
                                                 description=form.cleaned_data['description'],
                                                 category=form.cleaned_data['category'])
            new_price = ProductHistory.objects.create(purchase_price=form.cleaned_data['purchase_price'],
                                                      price_for_sale=form.cleaned_data['price_for_sale'])
            new_product.price_for_sale.add(new_price)           # łączymy nowy produkt z nową ceną zakupu. Wszytko łączy
            new_product.save()                                  # się w trzeciej tabeli i wyświetla na stronie
            return HttpResponseRedirect("/products")
        else:
            return render(request, "warehouse.html", {"form": form,
                                                        "products": products})

class EditProductCreatorView(View):
    def get(self, request, id):
        form = EditProductsForm()
        return render(request, "edit_product.html", {"form":form})

    def post(self, request, id):
        form = EditProductsForm(request.POST)
        if form.is_valid():
            edited_product = Product.objects.get(pk=id)
            edited_product.code = form.cleaned_data['code']
            edited_product.name = form.cleaned_data['name']
            edited_product.quantity = form.cleaned_data['quantity']
            edited_product.description = form.cleaned_data['description']
            edited_product.category = form.cleaned_data['category']
            edited_product.save()
            return HttpResponseRedirect("/products")