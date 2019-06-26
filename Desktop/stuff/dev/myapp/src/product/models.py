from django.db import models

# Create your models here.


class Product(models.Model):

    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField(default='this is cool')
    


# class Employee(models.Model):
#     title = models.CharField(max_length=120)
#     age = models.DecimalField(decimal_places=2, max_digits=1000)
#     position = models.CharField(max_length=120)

class Employee(models.Model):
    title = models.CharField(max_length=120, blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField(default='this is cool')

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.headline

class Students(models.Model):
    student_number = models.IntegerField(primary_key=True)
    f_name = models.CharField(max_length=20, blank=True, null=True)
    l_name = models.CharField(max_length=20, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=144, blank=True, null=True)
    county = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    gpa = models.IntegerField(blank=True, null=True)
 
  