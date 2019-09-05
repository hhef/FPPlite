from django.shortcuts import render
from django.views import View
from django.db.models import Q
from FPP.forms import CategoryForm, ContractorForm, ProductsForm, EditProductsForm, SaleContractorChooseForm, \
    SaleProductChooseForm, CategoryChoiseFieldForm
from django.http import HttpResponseRedirect
from FPP.models import Category, Contractor, Product, ProductHistory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class LandingPageView(View):
    def get(self, request):
        return render(request, "landing_page.html")


class WarehouseView(View):
    def get(self, request):
        products_list = Product.objects.order_by('code')
        paginator = Paginator(products_list, 5)
        page = request.GET.get("page", 1)
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        return render(request, "warehouse.html", {"products": products})

    def post(self, request):
        search = request.POST.get('search')
        products_list = Product.objects.filter(Q(name__icontains=search) | Q(code__icontains=search))
        return render(request, 'product_search.html', {"products_list": products_list})


class CreateCategoryView(View):
    def get(self, request):
        category = Category.objects.order_by('category')
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
        category = Category.objects.get(pk=id)
        products = Product.objects.filter(category=id)
        form = CategoryForm(instance=category)
        return render(request, "edit_category.html", {"form":form,
                                                      "products":products})

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
        contractors_list = Contractor.objects.order_by('name')
        form = ContractorForm()
        paginator = Paginator(contractors_list, 5)
        page = request.GET.get("page", 1)
        try:
            contractors = paginator.page(page)
        except PageNotAnInteger:
            contractors = paginator.page(1)
        except EmptyPage:
            contractors = paginator.page(paginator.num_pages)
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
        contractor = Contractor.objects.get(pk=id)
        form = ContractorForm(instance=contractor)
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
        form = ProductsForm()
        return render(request, "add_product.html", {"form":form})

    def post(self, request):
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
            return HttpResponseRedirect("/warehouse")
        else:
            return render(request, "add_product.html", {"form": form})


class EditProductCreatorView(View):
    def get(self, request, id):
        product = Product.objects.get(pk=id)
        form = EditProductsForm(instance=product)
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

class SaleView(View):
    def get(self, request):
        contractors = Contractor.objects.all()
        form = SaleContractorChooseForm()
        return render(request, "sale.html", {"form":form,
                                             "contractors":contractors})


    def post(self, request):
        form = SaleContractorChooseForm(request.POST)
        form_product = SaleProductChooseForm()
        if form.is_valid():
            contractor = form.cleaned_data['contractor']
            products = Product.objects.order_by('code')
            return render(request, "sale_product.html", {"form_product":form_product,
                                                         "products":products})