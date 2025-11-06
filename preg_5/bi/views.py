from django.shortcuts import render
from .models import Cliente, Pedido
from django.db.models import Sum, Count
from datetime import date

def consultas_view(request):
    cliente_especifico = Cliente.objects.get(nombre='Juan Perez')
    pedidos_cliente = Pedido.objects.filter(
        cliente=cliente_especifico,
        fecha_pedido__range=[date(2024, 5, 1), date(2024, 5, 31)]
    )

    clientes_sin_pedidos = Cliente.objects.exclude(pedido__isnull=False)

    cliente_unico = Cliente.objects.get(id=1)

    clientes_con_totales = Cliente.objects.annotate(
        total_pedidos=Count('pedido'),
        monto_total=Sum('pedido__monto')
    )

    context = {
        'pedidos_cliente': pedidos_cliente,
        'clientes_sin_pedidos': clientes_sin_pedidos,
        'cliente_unico': cliente_unico,
        'clientes_con_totales': clientes_con_totales,
    }

    return render(request, 'consultas.html', context)