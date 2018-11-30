from django.shortcuts import render

# Create your views here.
def s(req):
    return render(req,"h1.html")
