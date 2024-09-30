from django.http import HttpResponse

def  home(request):
    return HttpResponse("Hello world, you are at chai aur django homepage")

def  about(request):
    return HttpResponse("Hello world, you are at chai aur django about page")

def  contact(request):
    return HttpResponse("Hello world, you are at chai aur django contact page")