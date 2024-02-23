import pdb

from django import forms


class GameFacadeForm(forms.Form):
    game_sort = forms.ChoiceField(choices=[('dice', 'Бросаем кость'), ('coin', 'Подбрасываем монетку'),
                                           ('ticket', 'Смотрим номер лотерейного билета')],
                                  help_text="Что будем делать?")
    repetitions = forms.IntegerField(min_value=1, max_value=64, help_text="Сколько раз повторим?")

    def parse_response(self) -> dict[str, int]:
        pdb.set_trace()
        out = dict()
        reps, name = self.cleaned_data['repetitions'], self.cleaned_data['game_sort']
        for i in range(reps):
            out.setdefault(name, 0)
            out[name] += 1

        return out
