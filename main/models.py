import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('celana', 'Celana'),
        ('sepatu', 'Sepatu'),
        ('aksesoris', 'Aksesoris'),
        ('lainlain', 'Lain Lainnya')
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField(default = 0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='lain lain')
    is_featured = models.BooleanField(default = False)
    
    def __str__(self):
        return self.title
    