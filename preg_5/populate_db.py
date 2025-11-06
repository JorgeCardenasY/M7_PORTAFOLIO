import os
import django
from datetime import date


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'preg_5.settings')
django.setup()
from bi.models import Cliente, Pedido

def populate_db():
    # Crear clientes
    cliente1 = Cliente.objects.create(nombre='Juan Perez', email='juan.perez@example.com')
    cliente2 = Cliente.objects.create(nombre='Maria Garcia', email='maria.garcia@example.com')

    # Crear pedidos
    Pedido.objects.create(cliente=cliente1, fecha_pedido=date(2024, 5, 1), monto=100.00)
    Pedido.objects.create(cliente=cliente1, fecha_pedido=date(2024, 5, 15), monto=150.00)
    Pedido.objects.create(cliente=cliente2, fecha_pedido=date(2024, 5, 20), monto=200.00)
    Pedido.objects.create(cliente=cliente1, fecha_pedido=date(2024, 6, 1), monto=50.00)

if __name__ == '__main__':
    populate_db()