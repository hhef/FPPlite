from django import forms
from FPP.models import Category, Contractor


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class EditCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class ContractorForm(forms.ModelForm):
    class Meta:
        model = Contractor
        fields = "__all__"