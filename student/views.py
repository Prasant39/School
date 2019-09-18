from django.shortcuts import render
from django.http import HttpResponse
from .models import stud

def index(request):
    students = stud.objects.all().filter(roll="36535")    #fetches info from db
    context = {'students':students}
    return render(request,'index.html',context)

def details(request):
    if  request.method == "POST":
        name = request.POST.get("name")
        roll = request.POST.get("roll")
        semester = request.POST.get("semester")
        s = stud(naam=name, roll=int(roll),semester=int(semester))
       try:

           s.save()

       except:


           return HttpResponse("roll no.exists")
        

         return HttpResponse("your form has been submitted")
    else:        
        return render(request,'create.html')