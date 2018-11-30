from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,"h1.html")
def validate(request):
    user=request.POST.get("t1")
    pwd=request.POST.get("t2")
    res=request.POST.get("t3")
    d=["admin","user","employee"]
    c=["123","456","789"]
    a=["Admin","user","employee"]
    pos=d.index(user)
    if d[pos]==user and c[pos]==pwd:
        if a[pos]==res:
            mess=res
            return render(request, "h2.html", {"mes": mess})
        else:
            mess="it is not",res
            return render(request,"h1.html",{"mes":mess})

    else:
        mess="invalid username/password"
        return render(request,"h1.html",{"mes":mess})
