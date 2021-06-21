from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class FileStorage(models.Model):
    filename = models.CharField(max_length=200,blank=True)
    content = models.TextField(blank=True) 

    def __str__(self):
        return self.filename
    
     
 
    
