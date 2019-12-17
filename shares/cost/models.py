from django.db import models

# Create your models here.
class Share(models.Model):
	price=models.IntegerField(blank=True)
	leverage=models.IntegerField(blank=True)
	capital=models.IntegerField(blank=True)
