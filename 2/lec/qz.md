модель в django 	класс определяющий структуру таблиц бд
* Структура модели django 	аттрибут - поле таблицы; экземлпляр класса - запись(строка)
* класс-предок кастомных моделей	django.models.Model
* где создавать модели 	в том приложении которое работает с этими данными
* откуда импортируются типы полей 	django.models
* cтроковые типы(2) 	models.CharField; model.СharField;
* числовые типы(2) 	model.IntegerField, model.DecimalField,
* типы времени-даты 	model.DateField, model.DateTimeField
* внешний ключ 	model.ForeignKey
* распространённые параметры полей: максимальная длина строки; пустой? None? max_length; blank; null
* параметры даты: сейчас	auto_now_add=True
* поле картинки 	models.ImageField(upload_to='products/')
* поле, около-денежный формат 	models.DecimalField(max_digits = 8, decimal_places =2)
* django, библиотека для изображений	(pip install) Pillow
* миграция 	скрипт, меняющий структуру бд в соответствии с переменами моделей.
создаём миграции 	python manage.py makemigrations app_n
* путь к файлу миграций app_n/migrations
* нужно ли добавлять первичный ключ id 	нет, он генерируется
* применяем миграции 	python manage.py migrate
* как добавлять изменения 	пере(создать и применить) миграции
* путь к кастомным командам 	app_n/management/commands/comm.py; management и commands - пакеты(c инитом)
* от какого класса наследуются команды 	from django.core.management.base import BaseCommand 	
* как оформляется команда 	class Comm_n(BaseCommand): help="str" def handle(self,* args, ** kwargs): return
* вывод в консоль 	self.stdout.write("!")
* вызываем кастомную команду 	python manage.py Comm_n
* создаём-сохраняем экземпляр модели 	itm = ModelClassName(some="fields") itm.save()
* получаем все экземпляры(строки таблицы) itms = ModelClassName.objects.all()  self.stdout.write(f'itms')
* получаем один экземпляр/строку 	itm = ModelClassName.objects.get(id=stuff_from_kwargs)  self.stdout.write(f'{user}')
* добавляем аргумент в kwargs 	def add_arguments(self, parser): parser.add_argument('added_arg',type=int,help='descr')
* получаем None из пустой выборки вместо ошибки 	def handle(self,* args, ** kwargs): added_arg = kwargs['added_arg']  itm = ModelClassName.objects.filter(pk=pk).first()
* что означает агрумент pk в запросе MCN.filter(pk=pk)	primary key
* как добавляются агрументы-условия в MCN.filter()	MKN.objects.filter(ClassFieldName__condition=requested_value)
* пример условия: точно;в списке; в диапазоне 	exact; in; range
* пример условия: содержит, начинается с, заканчивается на 	contains, startswith, endswith
* приставка "без учёта регистра" 	i, как в exact, iexact
* пример условия: дата, год 	date, year
* фильтрующие функции(3) 	filter, get, exclude
* как делаем update, словами 	находим экземпляр через поиск(filter/get/exclude), переназначаем поля(itm.name="new"), сохраняем( itm.save())
* как делаем delete, словами 	находим экземпляр(filter/get/exclude); if itm is not None: itm.delete()
* как удалять то?	добавляем модели поле is_deleted = BooleanField() и его в случае удаления помечаем True
* каскадное удаление 	удаление дочерних записей объекта сразу после его удаления 
* внешний ключ, пример с каскадным удалением	local_field= models.ForeignKey(otherModelClass,on_delete=models.CASCADE)
* как вообще называть команды 	класс внутри всегда называется Command, а различаются они по именам файлов
* пример цепочки запросов 	itm1 = Model1.objects.get(pk=pk_arg).first()
if itm1 is not None:  goal = Model2.objects.filter(field=itm1)
* дополняем функционал моделей 	просто добавляем функции в классы и вызываем когда надо.