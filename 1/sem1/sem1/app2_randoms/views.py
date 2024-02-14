from typing import Callable
import logging
from django.shortcuts import render, HttpResponse

from random import choice

# Create your views here.
logger = logging.getLogger(__name__)


def caller_deco(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.debug(f"Was called {func.__name__}")
        return result

    return wrapper


def from_sample(population: int):
    return choice(range(population))


@caller_deco
def coin(request):
    return HttpResponse(from_sample(2))


@caller_deco
def dice(request):
    return HttpResponse(from_sample(6))


@caller_deco
def assassination(request):
    return HttpResponse(from_sample(100))
