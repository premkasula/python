from django.shortcuts import render

def show(req):
    d1={"id":"123",
        "na":"RAVI",
        "sal":"1259999.00",
        "desg":"CEO"}
    return render(req,"index1.html",d1)
