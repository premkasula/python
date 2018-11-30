from django.shortcuts import render

def check(request):
    return render(request,"check_box_list.html")
def play(request):
    song=request.POST.getlist("t1")
    song2 = request.POST.get("t2")
    song3 = request.POST.get("t3")
    song4 = request.POST.get("t4")
    
