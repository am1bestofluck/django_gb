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
* параметры даты 