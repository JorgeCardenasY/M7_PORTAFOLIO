from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Producto

class ProductoListView(ListView):
    model = Producto
    context_object_name = 'productos'
    template_name = 'productos/lista_productos.html'

class ProductoCreateView(CreateView):
    model = Producto
    fields = ['nombre', 'descripcion', 'precio', 'stock']
    template_name = 'productos/producto_form.html'
    success_url = reverse_lazy('lista_productos')

class ProductoUpdateView(UpdateView):
    model = Producto
    fields = ['nombre', 'descripcion', 'precio', 'stock']
    template_name = 'productos/producto_form.html'
    success_url = reverse_lazy('lista_productos')

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'productos/producto_confirm_delete.html'
    success_url = reverse_lazy('lista_productos')