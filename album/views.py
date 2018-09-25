from django.shortcuts import render
from django.http import HttpResponse
from album.models import Category, Photo 

def first_view(request):
    return HttpResponse('<h1>Esta es mi primera vista!</h1><h3>otra linea</h3>') 

def category(request):
    category_list = Category.objects.all()
    context = {'object_list': category_list}
    return render(request, 'album/category.html', context)