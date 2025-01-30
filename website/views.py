from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def bfsi(request):
    return render(request,"bfsi.html")