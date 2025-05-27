from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests 





@api_view(['POST'])
def access(request):
  content= {
  "access_status": True,
  "access_url": "https://techanugrahagroup.in/courses/java/"
}
  
  return Response(content)









@api_view(['POST'])
def token(request):
  print('token api..')
  key=request.headers.get('client_key')
  secreat=request.headers.get('CLIENT_SECRET')
  print('token api..1')

  try:
    responce=requests.post('https://sandbox-api.naanmudhalvan.in/api/v1/lms/client/token/',{      
        "client_key": key,
        "client_secret": secreat
    })
  except Exception as err:
      print(err)
    
  print('token api.. end')

  print(responce.json())  
  return Response(responce.json())






@api_view(['POST'])
def subscribe(request):
  content= {
"subscription_registration_status": True,
"subscription_reference_id": "123HJssjggI"
}
  
  return Response(content)

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
