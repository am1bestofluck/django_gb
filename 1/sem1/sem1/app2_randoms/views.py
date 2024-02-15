import pdb
from typing import Callable
import logging
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

from random import choice
from .models import CoinLogger

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
    result = from_sample(2)
    coin_itm = CoinLogger(result=result)
    coin_itm.save()
    return HttpResponse(result)


@caller_deco
def dice(request):
    return HttpResponse(from_sample(6))


@caller_deco
def assassination(request):
    return HttpResponse(from_sample(100))


def get_coins(request, qua):
    itms = CoinLogger.get_newest(qua)
    # pdb.set_trace()
    return JsonResponse(data=itms, safe=False)
