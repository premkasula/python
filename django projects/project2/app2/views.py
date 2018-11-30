from django.http import HttpResponse
from django.shortcuts import render




def show(seq):

    message="hello world"
    return HttpResponse(message)
