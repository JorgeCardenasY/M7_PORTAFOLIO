from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    productos = models.ManyToManyField(Producto, related_name='pedidos')
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Pedido #{self.id} de {self.cliente.nombre}"

    def save(self, *args, **kwargs):
        # Calcular el total del pedido antes de guardar (ejemplo simple)
        super().save(*args, **kwargs) # Guardar primero para tener un ID de pedido
        if not self.total and self.productos.exists():
            self.total = sum(producto.precio for producto in self.productos.all())
            super().save(update_fields=['total'])

