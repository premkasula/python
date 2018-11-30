from django.shortcuts import render

def login(request):
    return render(request,"login.html")
def validate(request):
    user=request.POST.get("t1")
    pwd=request.POST.get("t2")
    if user=="ravi" and pwd=="kumar":
        message="Ravi"
        return render(request,"welcome.html",{"message":message})
    elif user=="krishna" and pwd=="123@k":
        message="Krishna"
        return render(request,"welcome.html",{"message":message})
    elif user=="mohan" and pwd=="prasad":
        message="Mohan Prasad"
        return render(request,"welcome.html", {"message": message})
    elif user=="naveen" and pwd=="nnk":
        message="Naveen Kumar"
        return render(request,"welcome.html", {"message": message})
    else:
        message="inavlid username/password"
        return render(request,"login.html", {"message": message})