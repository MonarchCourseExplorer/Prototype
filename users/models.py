from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField('First Name', max_length= 120)
    last_name = models.CharField('Last Name', max_length= 120)
    email = models.EmailField(default= 'user@odu.edu')
    is_professor = models.BooleanField(default= False)

    def __str__(self):
        return self.first_name


class Professor(models.Model):
    first_name = models.CharField('First Name', max_length= 120)
    last_name = models.CharField('Last Name', max_length= 120)
    email = models.EmailField(default= 'user@odu.edu')
    is_professor = models.BooleanField(default= True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"




