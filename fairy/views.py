from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'fairy/main.html')


def quest(request):
    return render(request, 'fairy/quest.html')


def result(request):
    return render(request, 'fairy/result.html')