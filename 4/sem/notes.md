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

* зацикливаем форму(создали > вернулись к форме)  def add_stuff(request): 
  ...
  form.save()
  return redirect('add_stuff')
* в модели через ModelForm добавляем все поля кроме указанных   class SomeForm(forms.ModelForm):
  class Meta:
    model=FromModels
    exclude=['this_field']
* в модели через ModelForm пишем хинты для ввода  class SomeForm(forms.ModelForm):
  class Meta:
    model=FromModels
    labels={"field_of_model":"hint_for_template"}
# 4

автор - modelChoiceField(queryset=Author.objects.all())

* создаём объект  ModelName.objects.create(arg=item)

# 5
исправить view; только комментарий и автор
делаем редирект

# 6
написать про товары если нет;
по умолчанию в форме - то что уже и так в бд; редактирование - меняет бд.


