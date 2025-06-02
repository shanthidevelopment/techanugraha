from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import requests  as http
from website.models import Student
import jwt
import time

tokens={
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ4ODM0NTY2LCJpYXQiOjE3NDg4MzA5NjYsImp0aSI6IjBhYmRlMzJmMDM1NDQwODNhNzQ4NGMzYTE2YTA2MjVmIiwidXNlcl9pZCI6MzM5ODc1MSwiYXVkIjoibG9jYWxob3N0LDEyNy4wLjAuMSxhcGkubmFhbm11ZGhhbHZhbi50bi5nb3YuaW4sd3d3Lm5hYW5tdWRoYWx2YW4udG4uZ292LmluLHBvcnRhbC5uYWFubXVkaGFsdmFuLnRuLmdvdi5pbiwxMC4yMzYuMjMzLjE5OCwxOTIuMTY4LjguOSwxNjQuMTAwLjEzNC4zOSwxMC4yMzYuMjEwLjc3IiwiaXNzIjoiaHR0cHM6Ly93d3cubmFhbm11ZGhhbHZhbi50bi5nb3YuaW4vIn0.nUwNBl8zSVlTJCbf4ZyaqBqu3Q1k6p6hO7xFYhmjLWHhHeJLT56AWDrJgzk7dgI9hpsF9r6oNI_E6oMCzPFbvI1t-r5jTz7OwWSqPIuhEhKri7gTdpSurA72PZ_wspaQ3UhBY4Zs5-_I0jCGqtgg7SeOdPN3snHil6RQ1T1T9eU5ZG6jrOJnngoxp5BTlgtuQAd7Vx9Dg93_WvxHR6qOiKmIgWdvVM7OlWFchUwYxGJyFSdjKEetYSrseOfVe_A_0MnBR5jFr66-xg-koLeRM4KOOlZ1DP5-5b0lMaTIGQFfqWsHrVP7nPoVGEi3xc-Iz1Ua-m9cu3tSD_dlFNPZCQ",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0ODYzMTI1NiwiaWF0IjoxNzQ4NTQ0ODU2LCJqdGkiOiIwM2EyZTM5NTZlMDg0ZWNkYTFlZGY2NWEzOTlkNWZhNCIsInVzZXJfaWQiOjMzOTg3NTEsImF1ZCI6ImxvY2FsaG9zdCwxMjcuMC4wLjEsYXBpLm5hYW5tdWRoYWx2YW4udG4uZ292LmluLHd3dy5uYWFubXVkaGFsdmFuLnRuLmdvdi5pbixwb3J0YWwubmFhbm11ZGhhbHZhbi50bi5nb3YuaW4sMTAuMjM2LjIzMy4xOTgsMTkyLjE2OC44LjksMTY0LjEwMC4xMzQuMzksMTAuMjM2LjIxMC43NyIsImlzcyI6Imh0dHBzOi8vd3d3Lm5hYW5tdWRoYWx2YW4udG4uZ292LmluLyJ9.rbgH-XWufxMF-SBAY43bR6Ks3JMPIOJy40BGlm3q4NCSUMDYpx55Ulk5s03M9UWuJqQOb2IRdYJYnilH3TEtUUyCOLBedduYGCvdLLaITR7tvR02WW-vzdirb2WWgqdYFz9ASA9xBqkLXPDE9qIWOpRw6z_NLPkYG8aiBfGma0VFYmXO5vWhl5UA2YWY4E27CVdGVtNbfD4bSHsBJkJ2au4QWivUeYlQPPiXN7rQ_zA9OIJ-9zDnUuXn2oMHCoeiWu9Mi99ZNgK0gf0nSf9WbCKYlFHvJBJYaske_V_pBFrn_X4K71mtGYtAxSbsJGVYkxLkjedIdRf2jcKWhp1k0Q"
}

def getTokens():
    key='04ef11be66cea9786044632d25fc343a'
    secret='cb7bdaf3ab917e4a85f4f45f5245762b'
    global tokens
    print('Getting token for:', key)

    token = tokens.get('token')
    if token:
        try:
            # Decode JWT without verifying signature
            decoded = jwt.decode(token, options={"verify_signature": False})
            exp = decoded.get('exp')
            if exp and (exp - 300) > time.time():  # 5-minute buffer
                print("Using cached token.")
                return tokens
            else:
                print("Token expired or about to expire (within 5 mins).")
        except Exception as e:
            print("Error decoding token:", e)

    # Request new token
    print("Requesting new token...")
    response = requests.post(
        'https://api.naanmudhalvan.tn.gov.in/api/v1/lms/client/token/',
        json={
            'client_key': key,
            'client_secret': secret
        }
    )
    
    if response.status_code == 200:
        tokens = response.json()
        return tokens
    else:
        raise Exception(f"Failed to get token: {response.status_code}, {response.text}")
    


from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests  # Make sure you're using `requests` library, not `http`
# Assume `tokens` is defined somewhere in your code with the token key


@api_view(['POST'])
def access(request):
    # Log incoming data
    print(request.data)
    print('getting tokens')

    try:
        tokens = getTokens()
    except Exception as e:
        print("Error getting tokens:", e)
        return Response({"access_status": False, "error": "Token fetch failed"})

    # Incoming student info
    studentInfo = request.data

    # Prepare payload for external API
    payload = {
        "user_unique_id": studentInfo.get('user_id'),
        "course_unique_code": studentInfo.get('course_id')
    }

    headers = {
        'Authorization': 'Bearer ' + tokens['token'],
        'Content-Type': 'application/json'
    }

    # External API call
    try:
        response = requests.post(
            'https://api.naanmudhalvan.tn.gov.in/api/v1/lms/client/course/student/check/',
            json=payload,
            headers=headers
        )
        data = response.json()
        verified = data.get('status', False)
        print(data)
    except Exception as e:
        print("Error parsing response:", e)
        return Response({"access_status": False, "error": "Invalid response from external API"})

    if not verified:
        return Response({"access_status": False})

    # Save student data to DB
    try:
        student_data = {
            "user_id": studentInfo.get("user_id"),
            "student_name": studentInfo.get("student_name"),
            "college_code": studentInfo.get("college_code"),
            "college_name": studentInfo.get("college_name"),
            "branch_name": studentInfo.get("branch_name"),
            "district": studentInfo.get("district"),
            "university": studentInfo.get("university") or "",
            "email": studentInfo.get("email") or ""
        }

        student, created = Student.objects.get_or_create(
            user_id=student_data['user_id'],
            defaults=student_data
        )

        if not created:
            # Update only if student already exists
            for key, value in student_data.items():
                setattr(student, key, value)
            student.save()

        print("Student saved:", student)

    except Exception as e:
        print("Error saving student:", e)
        

    return Response({
        "access_status": True,
        "access_url": "https://techanugrahagroup.in/courses/tax/"
    })



@api_view(['POST'])
def token(request):
    # Get headers from request
    key = request.data.get('client_key')
    secret = request.data.get('client_secret') 
    tokens=getTokens()   
    
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
