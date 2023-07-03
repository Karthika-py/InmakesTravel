from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Team

# Create your views here.
# def index(request):
#     return render(request,"index.html")

def indexplace(request):
    obj=Place.objects.all()
    teamobj=Team.objects.all()
    return render(request,"index.html",{'result':obj,'teamresult':teamobj})



# def basic(request):
#     return render(request,"basic.html")


# def home(request):
#     return render(request,"home.html")
# def about(request):
#     return HttpResponse("About Me")
# def contact(request):
#     return render(request,"contact.html")
# def details(request):
#     return HttpResponse("More details:")
# def thanks(request):
#     return HttpResponse("Thank You.... Visit Again....")

# def objectparameter(request):
#     name="inmakes"
#     return render(request,"basic.html",{'obj':name})


# def index_add(request):
#     return render(request,"arithmetic.html")
#
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     sum=x+y
#     return render(request,"result.html",{'result':sum})