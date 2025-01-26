from django.shortcuts import render
from .models import Product, Student
from .forms import Productform
# Create your views here.

def home(request):
    if request.method == "POST":
       form = Productform(request.POST)
       if form.is_valid():
           nm = form.cleaned_data["name"]
           dc = form.cleaned_data["desc"]
           pr = form.cleaned_data["price"]
           reg = Product(name=nm, desc=dc, price=pr)
           reg.save()
           form = Productform()
    else:
        form = Productform()

    prod = Product.objects.all()
    stud = Student.objects.all()
    return render(request, "enroll/home.html", {"prod":prod, "form":form, "stud":stud})
