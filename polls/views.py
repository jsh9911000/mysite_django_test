from django.shortcuts import render
from django.http import Http404, HttpResponse

from polls.models import Question

# Create your views here. => 클라이언트의 요청(request)에 대해서 응답(response)해주는 함수 또는 클래스를 정의. 
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]   # Question 모델(DB)에서 해당 데이터를 5개만 가져온다.
    context = {                                         # json 처럼 탬플릿에 보내줄 데이터를 설정.
        "latest_question_list" : latest_question_list, 
    }
    return render(request, 'polls/index.html', context)  # 탬플릿을 리턴하면 데이터도 전송.

def detail(request, question_id):
    try:            # try 문.
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:         # except 문 => 데이터가 없다면 발생.
        raise Http404("Qustion does not exist")     # 404에러 발생시키면서 메세지 띄움.
    return render(request, 'polls/detail.html', {"question":question})  # 탬플릿을 리턴하면 데이터도 전송.

def results(request, question_id):
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s."%question_id)
