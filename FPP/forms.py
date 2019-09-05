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


class ProductsForm(forms.Form):
    code = forms.CharField(max_length=12)
    name = forms.CharField(max_length=256)
    quantity = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea)
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    purchase_price = forms.FloatField()
    price_for_sale = forms.FloatField()


class EditProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['price_for_sale']


class SaleForm(forms.Form):
    contractor = forms.ModelChoiceField(queryset=Contractor.objects.order_by('name'))
    product = forms.ModelChoiceField(queryset=Product.objects.order_by('code'))
    quantity = forms.IntegerField()
    price = forms.CharField()
