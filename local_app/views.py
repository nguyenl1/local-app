from django.shortcuts import render

def home(request):
    return render(request, "local_app/index.html")
    