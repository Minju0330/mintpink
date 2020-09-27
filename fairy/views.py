from django.shortcuts import render
from .models import Fairy

# Create your views here.

def main(request):
    return render(request, 'fairy/main.html')


def quest(request):
    return render(request, 'fairy/quest.html')


def result(request):
    arr = request.POST.get('arr')
    fairy = Fairy.objects.get(code=arr)
    context = {
        'fairy': fairy,
    }
    return render(request, 'fairy/result.html', context)