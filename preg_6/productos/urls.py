from django.urls import path
from .views import ProductoListView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView

urlpatterns = [
    path('', ProductoListView.as_view(), name='lista_productos'),
    path('nuevo/', ProductoCreateView.as_view(), name='crear_producto'),
    path('<int:pk>/editar/', ProductoUpdateView.as_view(), name='editar_producto'),
    path('<int:pk>/eliminar/', ProductoDeleteView.as_view(), name='eliminar_producto'),
]