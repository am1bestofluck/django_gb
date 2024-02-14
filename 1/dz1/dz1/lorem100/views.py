from typing import Callable

from django.shortcuts import render
from logging import getLogger

# Create your views here.

logger = getLogger(__name__)


def history(func: Callable):
    def wrapper(*args, **kwargs):
        nonlocal func
        out = func(*args, **kwargs)
        logger.info(f"{func.__name__}")
        return out

    return wrapper


@history
def lorems(request):
    return render(request, template_name="try_it.html")
