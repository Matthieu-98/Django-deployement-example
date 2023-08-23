from django.shortcuts import render
from .models import Member

def home(request):
    all_members = Member.objects.all
    return render(request, 'home.html',{'all':all_members})

def page_resto(request):
    return render(request, 'page_resto.html',{})
