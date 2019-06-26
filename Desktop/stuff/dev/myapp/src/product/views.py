from django.shortcuts import render

from .models import Product
from .models import Article
from .models import Employee
from .models import Students

# Create your views here.


def product_detail_view(request, *args, **kwargs):
    obj = Product.objects.all()
   #  context = {
    #    'title': obj.title,
    #   'description': obj.description
    # }
    context = {
        'object': obj
    }
    return render(request, 'product/detail.html', context)


def article_detail_view(request, *args, **kwargs):
    obj = Articles.objects.get(id=1)
   #  context = {
    #    'title': obj.title,
    #   'description': obj.description
    # }
    context = {
        'object': obj
    }
    return render(request, 'product/detail.html', context)



def students_detail_view(request, *args, **kwargs):
    obj = Employee.objects.get(id=1)
   #  context = {
    #    'title': obj.title,
    #   'description': obj.description
    # }
    context = {
        'object': obj
    }
    return render(request, 'product/detail.html', context)
