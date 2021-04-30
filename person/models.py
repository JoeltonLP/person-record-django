from django.db import models

class Person(models.Model):

    name = models.CharField('name', max_length=100)
    email = models.CharField('email', max_length=100, unique=True)
    phone = models.CharField('phone', max_length=100)


    def __str__(self):
        return f'{self.name} {self.phone}'
    
