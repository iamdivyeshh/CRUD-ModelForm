from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Students
from .forms import StudentForm
# Create your views here.


def add_show(request):
    if request.method == 'POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
           name = fm.cleaned_data['name']
           city = fm.cleaned_data['city']
           number = fm.cleaned_data['number']
           email = fm.cleaned_data['email']
           password = fm.cleaned_data['password']
           reg = Students(name=name, city=city, number=number, email=email, password=password)
           reg.save()
           fm = StudentForm()

    else:
        fm = StudentForm()
    stu = Students.objects.all()
    return render(request, 'main.html',{'form':fm, 'stu':stu})

def delete_data(reduest, id):
    if reduest.method == 'POST':
        stu = Students.objects.get(id=id)
        stu.delete()
    return HttpResponseRedirect('/')

def update_data(request, id):
    if request.method == 'POST':
        stu = Students.objects.get(id=id)
        fm = StudentForm(request.POST, instance=stu)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')
    else:
        stu = Students.objects.get(id=id)
        fm = StudentForm(instance=stu)
    return render(request, 'update.html',{'form':fm})   