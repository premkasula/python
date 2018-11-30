from django.shortcuts import render

# Create your views here.
def show(request):
    return render(request,"1st.html")
def how(req):
    so=req.POST.get("t1")
    mes=so
    return render(req,"1st.html",{"soo":mes})