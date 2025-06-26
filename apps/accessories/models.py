from django.db import models
from apps.terminals.models import Terminal


class Accessory(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    terminal = models.ForeignKey(
        Terminal,
        on_delete=models.CASCADE,
        related_name='accessories'
    )

    def __str__(self):
        return self.name
