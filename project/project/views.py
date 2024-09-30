from django.http import HttpResponse
from django.shortcuts import render

def  home(request):
    # return HttpResponse("Hello world, you are at chai aur django homepage")
    return render(request, 'index.html')
    # we can make any other folder inside the templates folder, let it be 'website'
    # and inside it be the index.html file
    # for that we have to write the path as : return render(request, 'website/index.html')

def  about(request):
    return HttpResponse("Hello world, you are at chai aur django about page")

def  contact(request):
    return HttpResponse("Hello world, you are at chai aur django contact page")