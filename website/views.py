from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import requests  as http
import asyncio

tokens={
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ4NTQ4NDU2LCJpYXQiOjE3NDg1NDQ4NTYsImp0aSI6IjI5MDg2ODE1OTg2ZDQxOGM4YTAxODk1OTFkNmEwMWY5IiwidXNlcl9pZCI6MzM5ODc1MSwiYXVkIjoibG9jYWxob3N0LDEyNy4wLjAuMSxhcGkubmFhbm11ZGhhbHZhbi50bi5nb3YuaW4sd3d3Lm5hYW5tdWRoYWx2YW4udG4uZ292LmluLHBvcnRhbC5uYWFubXVkaGFsdmFuLnRuLmdvdi5pbiwxMC4yMzYuMjMzLjE5OCwxOTIuMTY4LjguOSwxNjQuMTAwLjEzNC4zOSwxMC4yMzYuMjEwLjc3IiwiaXNzIjoiaHR0cHM6Ly93d3cubmFhbm11ZGhhbHZhbi50bi5nb3YuaW4vIn0.WmRoVcktpWpdy3uu17AlS0prHZWbaqWXd6HSIxeUHAk_bpcufba3JOX8wadfbnqRHJbMQz-FQwOf5FJ4RkVT3dmSBb2eGdb2QEsUZLq2SMc7JM4n-PbbbXlmP75H2BJiryJQlHEXa7C-AQlSA3qYvUWkyswjp6WUjRpIBeXplslrB7l8OVpLmCXsVwd5OOd-0-4ZtNVoiY6y7RHvMAKNIxb9Fw5F32bOUGchK1yhMtq3z2gk3IDPaphd2YAro4heGHN8TYxEnOBdHinEqgNDMIiyWwiK6CJc40u7dDfDe50_0iCSBWlt1yUz07XDtWaNQa82w4Go2pmTKfY5NZJjbg",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0ODYzMTI1NiwiaWF0IjoxNzQ4NTQ0ODU2LCJqdGkiOiIwM2EyZTM5NTZlMDg0ZWNkYTFlZGY2NWEzOTlkNWZhNCIsInVzZXJfaWQiOjMzOTg3NTEsImF1ZCI6ImxvY2FsaG9zdCwxMjcuMC4wLjEsYXBpLm5hYW5tdWRoYWx2YW4udG4uZ292LmluLHd3dy5uYWFubXVkaGFsdmFuLnRuLmdvdi5pbixwb3J0YWwubmFhbm11ZGhhbHZhbi50bi5nb3YuaW4sMTAuMjM2LjIzMy4xOTgsMTkyLjE2OC44LjksMTY0LjEwMC4xMzQuMzksMTAuMjM2LjIxMC43NyIsImlzcyI6Imh0dHBzOi8vd3d3Lm5hYW5tdWRoYWx2YW4udG4uZ292LmluLyJ9.rbgH-XWufxMF-SBAY43bR6Ks3JMPIOJy40BGlm3q4NCSUMDYpx55Ulk5s03M9UWuJqQOb2IRdYJYnilH3TEtUUyCOLBedduYGCvdLLaITR7tvR02WW-vzdirb2WWgqdYFz9ASA9xBqkLXPDE9qIWOpRw6z_NLPkYG8aiBfGma0VFYmXO5vWhl5UA2YWY4E27CVdGVtNbfD4bSHsBJkJ2au4QWivUeYlQPPiXN7rQ_zA9OIJ-9zDnUuXn2oMHCoeiWu9Mi99ZNgK0gf0nSf9WbCKYlFHvJBJYaske_V_pBFrn_X4K71mtGYtAxSbsJGVYkxLkjedIdRf2jcKWhp1k0Q"
}
def getTokens(key,secret):
    global tokens
    print('getting token',key,secret)
    if(tokens.get('token')):
        return tokens
    response = http.post(
            'https://api.naanmudhalvan.tn.gov.in/api/v1/lms/client/token/',
            json={
                'client_key': key,
                'client_secret': secret
            }
        )
    tokens = response.json() 
    return tokens
    



@api_view(['POST'])
def access(request):
  content= {
  "access_status": True,
  "access_url": "https://techanugrahagroup.in/courses/tax/"
}
  
  return Response(content)



@api_view(['POST'])
def token(request):
    # Get headers from request
    key = request.data.get('client_key')
    secret = request.data.get('client_secret') 
    global tokens
    getTokens(key,secret)
    
    # Send request to Naan Mudhalvan API
    
    
    return Response({
    "access_key": tokens['token'],
    "refresh_key": tokens['refresh']
    })
    




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
