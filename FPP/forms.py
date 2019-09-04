from django import forms
from FPP.models import Category, Contractor, Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class ContractorForm(forms.ModelForm):
    class Meta:
        model = Contractor
        fields = "__all__"


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"