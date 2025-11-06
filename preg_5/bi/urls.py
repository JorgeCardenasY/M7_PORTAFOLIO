from django.urls import path
from . import views

urlpatterns = [
    path('consultas/', views.consultas_view, name='consultas'),
]
