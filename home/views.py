# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def home(request):
   return render(request,"pages/home.html")

def header(request):
   return render(request,"content/header.html")

def menu(request):
   return render(request,"content/menu.html") 
 
