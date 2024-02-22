# 1
* выбираем игру через RadioInput или выпадающий список

через набор кортежей
itms = [(a,b),(c,d)]
choicesRow = forms.ChoiceField(choices=itms)
* для форм отображение через функции as_table - как таблица as_p - как параграф <p></p> as_b как блок <div></div>
* логика: проверяем пост; если нет - делаем форму; если да - проверяем поля, обрабатываем данные;

задаём описание поля 	field = forms.IntegerField(label="this you'll see")

class AuthorForm(form.ModelForm):
	class Meta:
		model = Author
		fields = ['name','emal']#etc
* кликаем альтом по переменным - так копируем :))
формы созданные через ModelForm делают валидацию сами и оформляют сохранение сами; мы же во вью только сохраняем их:
if request.method =="POST:
  form = AuthorForm(request.POST)
  if form.is_valid():
    form.save()
    return HttpResponse("ok") 

54!