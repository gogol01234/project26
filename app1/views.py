from django.shortcuts import render, redirect
from django.http import HttpResponse
from app1.models import *
from app1.forms import *
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == "POST":
        form = Form1(request.POST)
        if form.is_valid:
            name = request.POST["name"]
            messages1 = request.POST["messages"]
            email = request.POST["email"]
            print(name, email, messages1)
            contact2 = Model2( name = name , messages = messages1, email = email)
            contact2.save()
            messages.success(request, "Congratulations Your messages sent successfully!")
            return redirect("/")
            context = {
                "form":form
            }
    else:
        form = Form1()
        context = {
        "form":form
    }
    return render(request, "app1/home.html", context)


