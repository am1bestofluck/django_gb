реализация форм в django, импорт интструмента 	класс; fron django import forms
* где создаём формы 	в файле app/forms.py
* создаём форму Uform 	class Uform(form.Form): ...
* типы полей : текстовое поле; поле выбора; email 
form.CharField()
forms.EmailField()
forms.ChoiceField()
* типы полей: целое число, десятичное число, булево 	forms.IntegerField; forms.FloatField; forms.BooleanField;
* типы полей: загрузка img; загрузка файлов; дата/дата-время 	forms.ImageField; forms.FileField; forms.DateField/ forms.DateTimeField
* пример парсинга/рендера формы Uform 	def form_view(request):
  if request.method == "POST":
    form = UserForm( request.POST)
    if form.is_valid():
      name = form.cleaned_data['name']
      # обработка
  else:
    form = userForm()
    return render(request,'templates/app/form.html',{'form':'form})
* что нужно сделать для отображения формы 	пробросить её в в приложение и оттуда в проект через urls.py[urlpatterns]
* дорабатываем форму в шаблоне(2)	добавляем как переменную {{ form }}; дописываем кнопку submit
* пример формы CrossSiteForgeryAttack-proof 	
{% block content %}<form action="" method="POST">
	{% csrf_token %}
	{{ form }}
	<input type= "submit" value= "send"> </form>form> {% endblock %}
* получаем значения валидные значения из формы 	form.clearned_data
* выводим форму в шаблоне, каждый пункт - новый абзац<form mentod="post">... {{ form.as_p}} ..</form>
* виджет 	интерфейс, определяющий поведения поля ввода в шаблоне, заточенный под задачу
* примеры виджетов: несколько слов, почта, пароль 	textInput, EmailInput, PasswordInput
* примеры виджетов: флажок, выпадающий список, радио-выбор 	CheckboxInput, Select, RadioSelect
* примеры виджетов 	число, дата/дата-время, длинный текст	NumberInput, DateInput,DateTimeInput, Textarea
* как привязываем виджет к полю формы 	как аргумент вызова
* пример поля name "пара слов" с таким же виджетом в классе UForm 	class Uform(forms.Form):
  name = forms.Charfield(widget=forms.TextInput(attrs={'class':'form-control'}))
* даём виджету подсказку ко вводу ..widget = forms.TextInput('class':'form-control', placeholder='User friendly hint')
* булево Поле, не/обязательное для продолжение	is_unnecessary = forms.BooleanField(required = False)
* разворачиваем исключающее или 	either_or = forms.ChoiceField(choices=[('1','one'),('2','two')], widget = forms.RadioSelect(attrs={'class':'form-check-input'}))
* что в виджетах означают аттрибуты {attrs={'class':'form-check-input'|'form-control'}} 	это аттрибуты html элементов; конкретно эти - классы, которые уже есть в маппинге bootstrap
* bootstrap(4) 	фреймворк фронтэнд разработки; содержит html,css,js; строит responsive-дизайны; приоритет - мобильная разработка.
* поле  даты, оптимизирование ввода 	bdate = forms.DateField(initial = date.today(), attrs = {class='form-control', type='date'})
* штатная валидация полей формы 	form.is_valid() возвращает True если во вводе нет очевидных ошибок
* дополнительно проверяем поля 	создаём внутри класса формы функции clean_FieldName 
* пример валидации текста(name) 	def clean_name(self):
  name = self.cleaned_data['name']
  if True is False:
      raise forms.ValidationError("test case")
    return name
* сохраняем вывод формы в бд(4..5) 	сначала создаём-мигрируем модель бьющуюся с валидными полями формы(скорее vice-versa); дальше создаём экземляр модели с валидным выводом формы, ну и сохраняем; можно ещё логировать
* пример сохранения экз-ра модели из валидных данных формы 	..if form.is_valid():
  arg1 = form.cleaned_data['arg1']
  item = Item(arg=arg1)
  item.save()
* обратная связь по прогрессу/советы 	в представление добавляем одну строку и перезаписываем её по мере прогресса выполнения; возвращаем её состояние при рендеренге; как в get:заполните форму post: ошибка в начале обработки, если дошли до конца - ок.
* настраиваем проектный settings.py для работы с файлами  MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
* пример формы ImgForm для приёмки файлов/фото  class ImgForm(forms.Form):
form = forms.ImageField()
* импортируем модуль для работы с файлами   from django.core.files.storage import FileSystemStorage
* пример view для приемки файлов  def upload_image(request):
  if request.method == 'POST':
    form = ImageForm(request.POST, request.FILES)
      if form.is_valid():
        image = form.cleaned_data['image']
        fs = FileSystemStorage()
        fs.save(image.name,image)
      else:
        form = ImageForm()
      return return render(request,'path/to/t_form.html',{'form':form})
* обязательный аттрибут формы из шаблона для работы с файлами   enctype="multipart/form-data"
* пример формы для работы с файлами   <form method='post' enctype='multipart/form-data'>
  {% csrf_token ^%}
  {{ form_as_p }}
  <button type='submit'> Загрузить </button></form>