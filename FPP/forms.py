from django import forms
from FPP.models import Category, Contractor, Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class ContractorForm(forms.ModelForm):
    class Meta:
        model = Contractor
        exclude = ["debt"]


class ProductsForm(forms.Form):
    code = forms.CharField(max_length=12, label="Kod Produktu")
    name = forms.CharField(max_length=256, label="Nazwa Produktu")
    quantity = forms.IntegerField(label="Ilość")
    description = forms.CharField(widget=forms.Textarea, label="Opis")
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label="Kategoria")
    purchase_price = forms.FloatField(label="Cena zakupu")
    price_for_sale = forms.FloatField(label="Cena Sprzedaży")


class EditProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['price_for_sale']


class SaleContractorChooseForm(forms.Form):
    contractor = forms.ModelChoiceField(queryset=Contractor.objects.order_by('name'), label="Wybierz Kontrahenta")


class SaleProductChooseForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.order_by('code'), label="Wybierz Produkt")
    quantity = forms.IntegerField(label="Ilość")


class CategoryChoiseFieldForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label="Wybierz Kategorię")
