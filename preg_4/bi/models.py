from django.db import models

class Modelo1(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Modelo2(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

class Modelo3(models.Model):
    modelo1 = models.ForeignKey(Modelo1, on_delete=models.CASCADE, related_name='modelo3_set')
    modelo2 = models.ForeignKey(Modelo2, on_delete=models.CASCADE, related_name='modelo3_set')
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} of {self.modelo1.name} for {self.modelo2.title}"