from django.shortcuts import render


# Create your views here.

def lorems(request):
    return render(request, template_name="try_it.html")
