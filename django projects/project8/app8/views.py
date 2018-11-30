from django.shortcuts import render

def login(request):
    return render(request,"loginpage.html")
def validate(request):
    user=request.POST.get("t1")
    pwd=request.POST.get("t2")
    if user=="sathya" and pwd=="tech":
        message="Welcome to JINGA LALA"
        return render(request,"welcome.html",{"message":message})
    else:
        message="invalid username/password"
        return render(request,"loginpage.html",{"message":message})
