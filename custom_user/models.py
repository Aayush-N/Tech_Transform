from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
	total = models.IntegerField("Total", default=0)
	phone_no = models.CharField("Phone Number", max_length=12)

	
