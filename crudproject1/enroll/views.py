
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import User
from .forms import StudentRegistration

# Create your views here.
def add_show(request):
    if request.method =='POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            return HttpResponseRedirect('/')
    else:
        fm = StudentRegistration()
        stud = User.objects.all()
        return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':stud})
    
    #this function is for delete operation
def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/') 
    
   #this function is for update operation
def update_data(request, id):
    pi = get_object_or_404(User, pk=id)

    if request.method == 'POST':
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')  # redirect after successful POST
    else:
        fm = StudentRegistration(instance=pi)  # GET request, load form with data

    return render(request, 'enroll/updatestudent.html', {'form': fm})
