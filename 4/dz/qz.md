* что нужно в форме на уровне шаблона (3)	метод post; enctype; input:submit
* добавляем в проектные settings.py пути для клиентских файлов 	MEDIA_URL='/media/'
MEDIA_ROOT = BASE_DIR/ "media/"
* добавляем в проектный urls пути к клентским файлам(дебаг?) 	if settings.DEBUG:
    urlpatterns.extend(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
    urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
* откуда импортировать в проектном urls модули settings, static 	from django.conf.urls.static import static
from django.conf import settings
* добавляем в поля django форм аттрибуты html 	объявляем поле; в аргументы вызова добавляем widget; в агрументы виджета ложим словарь attrs= {"property":"value"}  title = forms.CharField(widget=forms.TextInput(attrs={"class": "form_fields"}))
* задём значение по умолчанию для поля формы 	self.fields['field'].initial=1
* что ложится в модели ImageField(upload_to=?) 	объект функции возвращающей путь/путевую строку
* аргументы функции для imageField(upload_to) 	user_directory_path(instance, filename), где instance - экземпляр из модели где вызван ImageField; filename - имя файла в момент передачи его в функцию; может отличаться на выходе.
* добавлям путь к динамическому файлу в view 	context['img_path']=model_instance.img_field.url
* декларируем форму с файлом в обработке post-запроса 	form = from_forms_py.CustomForm(request.POST,request.FILES)
* возвращаемся на страницу заполнения формы после валидной отправки 	return redirect("url_name_of_THIS_view",some="args")
* добавляем картинку в шаблон, после подготовки настроек проекта, и контекста вызова 	<img src= {{ key_from_context }}>
* пример формы для отправки файлов 	<form method="POST" action="" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="send photo">
</form>