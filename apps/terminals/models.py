from django.db import models

# Set a default "created_at" and "updated_at" fields in inheritance
class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Terminal model with the parameters from the CommonModel
class Terminal(CommonModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    in_stock = models.BooleanField()

    def __str__(self):
            return self.name

    class Meta:
        db_table = 'terminals'