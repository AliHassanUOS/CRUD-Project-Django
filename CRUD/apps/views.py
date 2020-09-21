from django.shortcuts import render, redirect
from django.http.response import HttpResponse, HttpResponseRedirect
from .forms import StudentRegistraion
from .models import Student


# Create your views here.

# Add Data and Show data Funcation
def home(request):
    if request.method == "POST":
        std = StudentRegistraion(request.POST)
        if std.is_valid():
            std.save()
            return redirect('home')
    else:
        std = StudentRegistraion()
        studentt = Student.objects.all()
        context = {
            'form': std,
            'studentt': studentt
        }
    return render(request, 'apps/home.html', context)


# This function will update Data


def update_data(request, id):
    if request.method == "POST":
        uid = Student.objects.get(pk=id)
        std = StudentRegistraion(request.POST, instance=uid)
        if std.is_valid():
            std.save()
    else:
        uid = Student.objects.get(pk=id)
        std = StudentRegistraion(instance=uid)
    context = {
        'form': std,
    }
    return render(request, 'apps/updatestudent.html', context)


# This function will delete data

def delete_data(request, id):
    if request.method == 'POST':
        dl = Student.objects.get(pk=id)
        dl.delete()
        return redirect('/')
