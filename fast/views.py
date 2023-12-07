from django.http import HttpResponse
from django.shortcuts import redirect, render
from fast.models import contract
from django.contrib import messages
import os
# Create your views here.

def home(request):
    return render(request,'ap/home.html')

def about(request):
    return render(request,'ap/about.html')

def index(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        sub=request.POST.get('sub')
        message=request.POST.get('message')
        values=contract(name=name,email=email,sub=sub,message=message)
        values.save()
        # return redirect('/')
    
    return render(request,'ap/index.html')

def blog(request):
    return render(request,'ap/blog.html')

def single_blog(request):
    return render(request,'ap/single-blog.html')

# def edit(request):
#     return render(request,'ap/edit.html')

def edit(request,id):
    edit=contract.objects.get(pk=id)
    if request.method=='POST':
        # if len(request.FILES) !=0:
        #     if len(edit.image)>0:
        #         os.remove(edit.image.path)
        #     edit.image=request.FILES['image']
        edit.name=request.POST.get('name')
        edit.email=request.POST.get('email')
        edit.sub=request.POST.get('sub')
        edit.message=request.POST.get('message')
        edit.save()
        
        return redirect('/home/')
    return render(request,"ap/edit.html",{'edit': edit})

def show(request):
    face=contract.objects.all()
    return render(request,'ap/show.html', {'tab':face})

def delt(request,id):
    dlt=contract.objects.get(pk=id)
    dlt.delete()
    return redirect('/sw/')

def animation(request):
    return render(request, 'ap/animation.html')
   