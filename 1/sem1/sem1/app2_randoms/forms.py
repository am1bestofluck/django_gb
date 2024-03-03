import pdb
import random

from django import forms


class GameFacadeForm(forms.Form):
    game_sort = forms.ChoiceField(choices=[('dice', 'Бросаем кость'), ('coin', 'Подбрасываем монетку'),
                                           ('ticket', 'Смотрим номер лотерейного билета')],
                                  )  # help_text="Что будем делать?")
    repetitions = forms.IntegerField(min_value=1, max_value=64, )  # help_text="Сколько раз повторим?")

    def parse_response(self) -> dict[str, int]:
        out = dict()
        reps, name = self.cleaned_data['repetitions'], self.cleaned_data['game_sort']
        out["name"] = name
        out["result"] = dict()
        match name:
            case "coin":
                limit = 2
            case "dice":
                limit = 6
            case "ticket":
                limit = 100
            case _:
                limit = 1
        for i in range(reps):
            tmp = random.randint(1, limit)
            out['result'].setdefault(tmp, 0)
            out["result"][tmp] += 1
        return out
