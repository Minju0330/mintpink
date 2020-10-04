from django.shortcuts import render, HttpResponse
from .models import Fairy, Quest
import json


# Create your views here.

def main(request):
    return render(request, 'fairy/main.html')


def quest(request):
    quest = Quest.objects.get(pk=1)
    context =  {
        quest: 'quest',
    }
    return render(request, 'fairy/quest.html', context)


def quest_data(request):
    num = request.POST.get('num')
    quest = Quest.objects.get(pk=num)
    context = {
        'pk': quest.pk,
        'content': quest.content,
        'answer1': quest.answer1,
        'answer2': quest.answer2,
    }
    return HttpResponse(json.dumps(context), content_type="application/json")


def result(request):
    arr = request.POST.get('arr')
    fairy = Fairy.objects.get(code=arr)
    context = {
        'fairy': fairy,
    }
    return render(request, 'fairy/result.html', context)