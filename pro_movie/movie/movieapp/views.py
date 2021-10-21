from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import movie
from .form import movieform
# Create your views here.
def home(request):
    obj = movie.objects.all()
    return render(request,'home.html',{'movie':obj})
def details(request,movie_id):
    obj = movie.objects.get(id=movie_id)
    return render(request,'details.html',{'movie':obj})
def addi(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        des = request.POST.get('desc',)
        year = request.POST.get('year',)
        image = request.FILES['img']
        obj=movie(name=name,description=des,year=year,image=image)
        obj.save()
    return render(request,'add.html')
def update(request,id):
    obj = movie.objects.get(id=id)
    form=movieform(request.POST or None,request.FILES, instance=obj)
    if form.is_valid():
        form.save()
        return  redirect('/')
    return render(request,'edit.html',{'form':form,'movie':obj})
def delete(request,id):
    if request.method =='POST':
        obj=movie.objects.get(id=id)
        obj.delete()
        return redirect('/')
    return render(request,'delete.html',)