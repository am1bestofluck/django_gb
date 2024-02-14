from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return HttpResponse(
        '<div style="display:flex;align-content: center;justify-content: center;"><iframe width="560" height="315" src="https://www.youtube.com/embed/q85zE0JQamc?si=dCovomlvYQqKCrY3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></div>')
