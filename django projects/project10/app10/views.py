from django.shortcuts import render
def lang(request):
    return render(request,"checkbox.html")
def check(request):
    res=request.POST.getlist("t1")
    if res!=None:
        message=res
        return render(request,"checklist.html",{"message":message})
    else:
        message="please select atleast one"
        return render(request,"checkbox.html",{"message":message})
