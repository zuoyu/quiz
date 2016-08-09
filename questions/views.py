from django.shortcuts import render, get_object_or_404
from .models import Question, Answer
import uuid

def index(request):
    question_list = Question.objects.order_by('-pub_date').reverse()
    context = {'question_list': question_list}
    return render(request, 'index.html', context)

def submit_quiz(request):
    anonymouse_user_session = uuid.uuid1()
    print anonymouse_user_session
    for key in request.POST.iterkeys():
        if key.startswith('answer-'):
            question = Question.objects.get(pk=int(key[7:]))
            answer = Answer.objects.create(question=question, anwser_text=request.POST[key], session=anonymouse_user_session)
    return render(request, 'submitted.html')
