from django.shortcuts import render
from django.http import HttpResponse

from .form import ProjectForm

from hello_world.models import Project


# Create your views here.


def hello_world(request, *args, **kwargs):
        # return HttpResponse("<h1>hello world</h1>")
    return render(request, 'hello_world.html', {})


def contact_views(request, *args, **kwargs):
    return render(request, 'contact.html', {})


def project_views(request):
    obj = Project.objects.get(id=1)
    # # context = {
    # #     # 'title': obj.title,
    # #     # 'describe': obj.describe,
    # #     # 'technology': obj.technology
    # }
    context = {
        'object': obj
    }
    return render(request, 'project/project.html', context)


def project_create_view(request):
   form = ProjectForm(request.POST or None)
   if form.is_valid():
   		form.save()
   		form = ProjectForm()
   context = {
   		'form': form
   	}
   return render(request, 'project/project_create.html', context)
