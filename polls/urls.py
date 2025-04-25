from django.urls import path 
from . import views 

urlpatterns = [
    # 최상위 앱 mysite의 urls.py로부터 전달받으면, path()에서 첫번째 매개변수로 파라미터를 설정하는데 "" 비어 있기 때문에, 127.0.0.1/polls/로 url은 전달되고 views.py의 index 함수가 실행이 된다.
    path("", views.index, name="index")  
]