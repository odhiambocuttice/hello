from django.contrib import admin

# Register your models here.
from .models import Product
from .models import Article
from .models import Employee
from .models import Students


admin.site.register(Product)
admin.site.register(Article)
admin.site.register(Employee)
admin.site.register(Students)
