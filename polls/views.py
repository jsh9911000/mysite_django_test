from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. => 클라이언트의 요청(request)에 대해서 응답(response)해주는 함수 또는 클래스를 정의. 
def index(request):
    return HttpResponse("Hello World.")