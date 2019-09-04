from django.shortcuts import render
from django.views import View
from FPP.forms import CategoryForm, ContractorForm, ProductsForm
from django.http import HttpResponseRedirect
from FPP.models import Category, Contractor, Product


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
        products = Product.objects.order_by('name')
        form = ProductsForm()
        return render(request, "warehouse.html", {"form":form,
                                                    "products":products})

    def post(self, request):
        products = Product.objects.order_by('name')
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/products")
        else:
            return render(request, "warehouse.html", {"form": form,
                                                        "products": products})