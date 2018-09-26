from django.shortcuts import render
from django.http import HttpResponse
from album.models import Category, Photo 
from django.views.generic import ListView, DetailView

#def first_view(request):
 #   return HttpResponse('<h1>Esta es mi primera vista!</h1><h3>otra linea</h3>') 
def base(request):
    return render(request, 'base.html')

def category(request):
    category_list = Category.objects.all()
    context = {'object_list': category_list}
    return render(request, 'album/category.html', context)


def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    context = {'object': category}
    return render(request, 'album/category_detail.html',context)


class PhotoListView(ListView):
    model = Photo

class PhotoDetailView(DetailView):
    model = Photo