from django.shortcuts import render

# Create your views here.
def show(req):
    return render(req,"1st.html")
def snow(req):
    res=req.POST.getlist("s1")
    return render(req,"1st.html",{"res":res})