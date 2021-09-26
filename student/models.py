from django.db import models

# Create your models here.

class Filier(models.Model):
    filier = models.CharField(max_length=80)
    def __str__(self):
        return self.filier

class Students(models.Model):
    f_name = models.CharField(max_length=250)
    l_name = models.CharField(max_length=250)
    filier = models.ForeignKey(Filier,name='filiers',on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.f_name} {self.l_name}"