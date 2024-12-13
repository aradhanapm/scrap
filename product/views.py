from django.shortcuts import render
from product.forms import ProductAddForm,CategoryForm
from product.models import Products,Category
from django.urls import reverse,reverse_lazy
from django.views.generic import CreateView,UpdateView,ListView,DeleteView

class categoryAddView(CreateView):
    template_name="category.html"
    model=Category
    form_class=CategoryForm
    context_object_name="data"

    def get_success_url(self):
        return reverse("index")
    

class ProductAddView(CreateView):
    template_name="add.html"
    model=Products
    form_class=ProductAddForm
    context_object_name="data"

    def get_success_url(self):
        return reverse("index")
    
class ProducteditView(UpdateView):
    template_name="edit.html"
    model=Products
    form_class=ProductAddForm
    context_object_name="data"

    def get_success_url(self):
        return reverse("index")

class indexView(ListView):
    template_name="index.html"
    model=Products
    form_class=ProductAddForm
    context_object_name="data"

    def get_success_url(self):
        return reverse("index")
    def get_success_url(self):
        return render("index")

class delView(DeleteView):
    template_name="delete.html"
    model=Products
    success_url=reverse_lazy("index")
    

# Create your views here.

