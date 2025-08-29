from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data= {
        'title':'Wscubetech Home Page',
        'clist':['Python','Django','Flask'],
        'student_details':[
            {'name':'pradeep','phone':9258645756},
            {'name':'testing','phone':9258645757}
        ]
    }
    return render(request,"index.html",data)

def aboutUS(request):
    return HttpResponse("Welcome to Wscubetech");

def course(request):
    return HttpResponse("welcome to wscubetech")

def courseDetails(request,courseid):
    return HttpResponse(courseid)

