"""
최상위 URLconf.
클라이언트의 요청 url에 따라 path()에서 여러 앱의 URLconf(urls.py)로 연결시켜준다.
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")), # 127.0.0.1/polls/ 라는 요청이 오면, poll/ 경로는 polls 앱의 urls.py로 연결시켜준다.
    path('admin/', admin.site.urls),
]
