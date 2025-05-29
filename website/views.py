from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import requests  as http





@api_view(['POST'])
def access(request):
  content= {
  "access_status": True,
  "access_url": "https://techanugrahagroup.in/courses/java/"
}
  
  return Response(content)







@api_view(['POST'])
def token(request):
    # Get headers from request
    key = request.data.get('client_key')
    secret = request.data.get('client_secret') 
    
    # Send request to Naan Mudhalvan API
    # response = http.post(
    #         'https://api.naanmudhalvan.tn.gov.in/api/v1/lms/client/token/',
    #         json={
    #             'client_key': key,
    #             'client_secret': secret
    #         }
    #     )

    # print('Token API completed.')
    # data=response.json()  
    
#     return Response({
#   "access_key": data['token'],
#   "refresh_key": data['refresh']
# })
    return Response({
    "access_key": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ4NTQzMjA1LCJpYXQiOjE3NDg1Mzk2MDUsImp0aSI6IjkwNWE5NTcxMDVmNTQwNTRiOTYzYjU3ZDVjNzdhYmYyIiwidXNlcl9pZCI6MzM5ODc1MSwiYXVkIjoibG9jYWxob3N0LDEyNy4wLjAuMSxhcGkubmFhbm11ZGhhbHZhbi50bi5nb3YuaW4sd3d3Lm5hYW5tdWRoYWx2YW4udG4uZ292LmluLHBvcnRhbC5uYWFubXVkaGFsdmFuLnRuLmdvdi5pbiwxMC4yMzYuMjMzLjE5OCwxOTIuMTY4LjguOSwxNjQuMTAwLjEzNC4zOSwxMC4yMzYuMjEwLjc3IiwiaXNzIjoiaHR0cHM6Ly93d3cubmFhbm11ZGhhbHZhbi50bi5nb3YuaW4vIn0.W356Tprec1L5YhwOhSy05fxyUaERtD-pgo10VdNoRSBAZrS0xWvGuMCr3vW04hJLpAjuCnNOiwXp3LR9UfiOt37RUGHv8B1T66a39_63A_YLEE41jXI7z1qyWvywq7RDPMKb8e4L8grIhmNbD44SYrFmAgvDK5pmjjwaTAys6HRqPbQG4zJSQLUYvRNfKwHrp53tWXG4GsAtBwEEW9CtRY1NLGs1sWLR4o_7_-8bRozsN-wGeeUmJfUFlR4z2aIpTRHDoufBcc_tWjhAvN2lnirv8n1BwBDQ9D0o07kumaro2EIPkmuoe_U7MqPK3W26Ue-YYJE_CSTVyHWazZ2W5g",
    "refresh_key": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0ODYyNjAwNSwiaWF0IjoxNzQ4NTM5NjA1LCJqdGkiOiJkNjFjZDI2MDUwZGM0Zjc3OWQ0ZjdmZTM5MDU5NDM4OCIsInVzZXJfaWQiOjMzOTg3NTEsImF1ZCI6ImxvY2FsaG9zdCwxMjcuMC4wLjEsYXBpLm5hYW5tdWRoYWx2YW4udG4uZ292LmluLHd3dy5uYWFubXVkaGFsdmFuLnRuLmdvdi5pbixwb3J0YWwubmFhbm11ZGhhbHZhbi50bi5nb3YuaW4sMTAuMjM2LjIzMy4xOTgsMTkyLjE2OC44LjksMTY0LjEwMC4xMzQuMzksMTAuMjM2LjIxMC43NyIsImlzcyI6Imh0dHBzOi8vd3d3Lm5hYW5tdWRoYWx2YW4udG4uZ292LmluLyJ9.u0mdncI0T9WPucjKLlnAFfZFXvU3I9-ORhvfxiuuwGAFYpxp-4_0KokwpzFWV7mN0mntwUFz76eTZmKOZIIgl3v0HkQn_pNTkQXaaiOKqLHlC4IZe7yREERXSJF-SBfPx7zhz-S_XRyapzoHCs5PWDnLxEp3X43gvRw7_zUl9kMOHxA3RVnNPXf0aK2tW26j8v7YLMY_za4pVJmt-QdMlY_1EHzXJXLn8TtHImJ_iXsYL7UHB_TP5QbYHHBL1oJVFybUes1tUVykR38dhvWIe3-FnDjP-JkfQ2ENWSqpTGoRwRyEOtXTo03MhUMYpx3QyvbpLBRh_D13s47o8V8xWA"
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
