from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def bfsi(request):
    return render(request,"bfsi.html")


def cpp_view(request):
    return render(request, 'cpp.html')


def java(request):
    return render(request, 'java.html')


def python(request):
    return render(request, 'python.html')


def web(request):
    return render(request, 'web.html')


def mern(request):
    return render(request, 'mern.html')


def mob(request):
    return render(request, 'mob.html')

def react(request):
    return render(request, 'react.html')


def sql(request):
    return render(request, 'sql.html')


def ecom(request):
    return render(request, 'ecom.html')


def dm(request):
    return render(request, 'dm.html')


def report(request):
    return render(request, 'report.html')


def custom(request):
    return render(request, 'custom.html')


def business(request):
    return render(request, 'business.html')


def tax(request):
    return render(request, 'tax.html')
