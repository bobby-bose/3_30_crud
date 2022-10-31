from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def home(request):
    if request.method=="POST":
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        obj=Student()
        obj.fname=fname
        obj.lname=lname
        obj.save()
        print("The data ",fname,"and",lname,"is saved")
        if fname=="admin" and lname=="admin":
            return redirect("success")
    context={"message":"Welcome akshaya"}
    return render(request,"home.html",context)

def success(request):
    return render(request,"success.html")

def details(request):
    data=Student.objects.all()
    context={"data":data}
    return render(request,"details.html",context)

def delete(request,id):
    data=Student.objects.get(id=id)
    data.delete()
    return redirect("details")

