from django.shortcuts import render

def show(request):
    return render(request,"index.html")
def showDetails(request):
    id=request.POST.get("t1")
    name=request.POST.get("t2")
    salary=request.POST.get("t3")
    designation=request.POST.get("t4")

    d1={"IDNO":id,
        "NAME":name,
        "SALARY":salary,
        "DESIGNATION":designation,
        }
    return render(request,"index1.html",d1)

