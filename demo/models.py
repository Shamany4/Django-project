from django.db import models

# python manage.py makemigrations
# python manage.py migrate

# Create your models here.

class Book(models.Model):
	title = models.CharField(max_length=40, blank=False, unique=True)
	description = models.TextField(max_length=500, blank=True)
	price = models.DecimalField(default=0, max_digits=5, decimal_places=2)
	published = models.DateField(null=True)
	is_published = models.BooleanField(default=False)
	cover = models.ImageField(upload_to='covers/', height_field=150, width_field=75, default=0)