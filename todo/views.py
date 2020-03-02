from django.shortcuts import render,redirect
from .models import List
from .forms import ListForm

# Create your views here.

def home(request):
    all_items = List.objects.all()
    return render(request,'todo/home.html',{'all_items':all_items})

def add(request):
    if request.method == 'POST':
        gfgf = request.POST['text']
        text = List(text=gfgf)
        text.save()
        return redirect('home')
    return render(request,'todo/home.html')

def delete(request,idd):
    th = List.objects.filter(id=idd).delete()
    return redirect('home')


def update(request,idd):
    text = List.objects.get(id=idd)
    form = ListForm(instance=text)
    if request.method == 'POST':
        form = ListForm(request.POST,instance=text)
        form.save()
        return redirect('home')
    return render(request,'todo/update.html',{'form':form})


def uncomplite(request,idd):
    item = List.objects.get(pk=idd)
    item.complite = False
    item.save()
    return redirect('home')

def complite(request,idd):
    item = List.objects.get(pk=idd)
    item.complite = True
    item.save()
    return redirect('home')