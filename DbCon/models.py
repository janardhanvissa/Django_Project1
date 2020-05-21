from django.forms import ModelForm, Textarea
from django.db import models


# Create your models here.
class Students(models.Model):
	Sid = models.CharField(max_length=20)
	f_name = models.CharField(max_length=100)
	l_name = models.CharField(max_length=15)
	email = models.EmailField(max_length=100)


class Meta:
	db_table = "students"
