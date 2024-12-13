from django import forms
from product.models import Products,Category




class ProductAddForm(forms.ModelForm):
    class Meta:
        model=Products
        exclude=("user","status")
class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields="__all__"