from django.db import models

# Create your models here.

class Portfolio(models.Model): # class는 항상 대문자로 시작을 해야한다.
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='./images/')
    description = models.CharField(max_length=500)
    
    def __str__(self):
        return self.title