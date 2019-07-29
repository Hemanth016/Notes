# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from models import Note

def index(request):

    if request.method == 'POST':
        title=request.POST['title']
        text=request.POST['text']
        note=Note(title=title,text=text)
        note.save()
    else:
        return render(request,'webApp/index.html')

# Create your views here.
