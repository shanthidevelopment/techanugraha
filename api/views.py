from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def demo(request):
    content={
        'msg':"Welcome to techanugraha"
    }
    return Response(content)

@api_view(['POST'])
def access(request):
  content= {
  "access_status": True,
  "access_url": "https://techanugrahagroup.in/courses/java/"
}
  
  return Response(content)
