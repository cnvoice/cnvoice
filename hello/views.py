from django.shortcuts import render
from django.http import JsonResponse

from .encrypt import sentencize


def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def encrypt(request):
    content = request.POST.get('content', None)
    data = {
        'encrypted_content': sentencize(content)
    }
    return JsonResponse(data)