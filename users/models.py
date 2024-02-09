
from django.db import models
from django.contrib.auth.models import User


class Advertisement(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    photo1 = models.ImageField(upload_to='ad_photos/', null=True, blank=True)
    photo2 = models.ImageField(upload_to='ad_photos/', null=True, blank=True)
    photo3 = models.ImageField(upload_to='ad_photos/', null=True, blank=True)
    number_phone = models.DecimalField(max_digits=10, decimal_places=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title