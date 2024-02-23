import pdb
from typing import Callable
import logging
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.views.generic import View, FormView

from random import choice
from .models import CoinLogger
from . import forms as MyForms

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


def coin_no_deco(request):
    result = from_sample(2)
    # coin_itm = CoinLogger(result=result)
    # coin_itm.save()
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


def throw_all_coins(request, qua):
    throws = {True: 0, False: 0}

    for i in range(qua):
        throws[bool(int(coin(request).content))] += 1
    return "boring."


class ThrowAllCoins(View):
    template_name = "app2_randoms/many_coins.html"

    def get(self, request, **kwargs):
        # pdb.set_trace()
        qua = kwargs['qua']
        context = {'title': f'Throw {qua} coins! Such a waste!', "result": {True: 0, False: 0}}

        for i in range(qua):
            context['result'][bool(int(coin_no_deco(request).content))] += 1
        return render(request, self.template_name, {"context": context})


class GamesFacade(FormView):
    template_name = "app2_randoms/games_facade.html"
    form_class = MyForms.GameFacadeForm
    success_url = "app2_randoms/facade_result.html"

    def form_valid(self, form: MyForms.GameFacadeForm):
        context = {"title": f"Result of {form.cleaned_data['game_sort']} for {form.cleaned_data['repetitions']} times",
                   "out": form.parse_response()}
        pdb.set_trace()
        return super().form_valid(form)
