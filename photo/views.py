from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView




from .models import Photo

# Create your views here.

def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photos':photos})