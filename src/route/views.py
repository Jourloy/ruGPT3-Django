from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from torch import constant_pad_nd

from route.generate.ruTitle import RuTitle
from route.generate.ruGPT3 import RuGPT3
from route.generate.ruDolph import RuDolph


def gpt3(request):
    text = request.GET.get('text', '')
    maxLength = int(request.GET.get('maxLength', '0'))

    gen = ''

    try:
        gpt3 = RuGPT3()
        gen = gpt3.generate(text, maxLength)
    except:
        gen = text
    return HttpResponse(gen)


def title(request):
    text = request.GET.get('text', '')

    gen = ''

    try:
        title = RuTitle()
        gen = title.generate(text)
    except:
        pass

    return HttpResponse(gen)


def image(request):
    text = request.GET.get('text', '')

    try:
        img = RuDolph()
        image = img.generate(text)
        response = FileResponse(image)
        return response
    except:
        return HttpResponse('500 error')
