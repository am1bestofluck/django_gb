from django.shortcuts import render, HttpResponse


# Create your views here.

def get_yt(request):
    return HttpResponse(
        '<div style="display:flex;justify-content: center;"><iframe width="560" height="315" src="https://www.youtube.com/embed/Uyft9x-UP40?si=ogiR16k3kcECUS6R" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></div>')
