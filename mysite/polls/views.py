from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list':latest_question_list}
    #output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse("you are looking at Ques %s." % question_id)

def results(request, question_id):
    response =" you are looking at Result ques %s."
    return HttpResponse (response % question_id)

def vote(request, question_id):
    return HttpResponse ("you'r Voting on ques %s." % question_id)



# Create your views here.
