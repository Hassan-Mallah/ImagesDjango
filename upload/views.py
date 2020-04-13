# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .forms import *
from django.shortcuts import render,get_object_or_404

# Create your views here.


def home(request):
    images = Image.objects.all()
    context = {'images': images}
    return render(request, 'home.html', context)


def upload(request):
    if request.method == 'POST':
        form = ImagesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ImagesForm()
    return render(request, 'upload.html', {'form': form})


def viewImage(request, id):
    obj = get_object_or_404(Image, id=id)
    return render(request, 'viewImage.html', {'obj': obj})