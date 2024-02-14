mvt, расшифровка 	model view template
* реализация model	таблицы бд
* реализация view 	функции и классы; обрабатывают запросы и формируют ответы
* реализация template 	шаблоны (веб)страниц, ui
* роль маршрутов 	связывают view(представление) и template(шаблон)
* устанавливаем django 	pip install django
* разница между django проектом и приложением 	приложение -  агрегационный блок проекта; то и другое - пакеты python.
* создаём django проект 	django-admin startproject prj_name
* миграции django 	курирование бд
* роль файла manage.py(3+) 	запуск,миграции, контроль учётных записей и др.
* роль urls.py 	маршрутизация
* роль setting.py 	настройки, пути к объектам( бд, статика и др.)
* роль asgi.py wsgi.py 	интерфейсы для запуска согласно своим названиям
* asgi 	Asynchronous Server Gateway Interface, наследник wsgi; соглашение для веб-серверов обрабатывать запросы единым интерфейсом, асинхронно
* wsgi Web Server Gateway Interface - соглашение единого интерфейса для разных реализаций серверов
* запускаем django проект 	python manage.py runserver
* меняем сайт/порт запуска 	python manage.py runserver 127.0.0.2:80
* добавляем допустимые хосты  	в settings.py добавляем ALLOWED_HOSTS = [192.168.1.184]
* создаём новое приложение 	python manage.py startapp app_name
* добавляем приложение в проект 	в settings.py: INSTALLED_APPS = [ app_name ]
* импортируем реализацию веб-страницы 	from django.http import HttpResponse
* простейший маршрут 	def index(request):  return Httpresponse("Hellow")
* что принимает вью функция 	запрос от пользователя(request)
* импортируем машршрут 	from django.urls import path
* пример маршрута 	urlpatterns = [path('link/',app_name.module_name.func_name)]
* что делает django.urls.include 	перехватывает адрес и отдаёт его в приложение 	path('',include(my_app.urls))
* структура url.py в рамках проекта 	в приложениях хардлинки внутри urls.py; в головном (проектном) urls. py - path("link/",include(app_name.urls)
* пример маршрута в приложении 	urlpatterns = [path('from_main_project/',app_views.func_view,name="route_name")]
где описываем логирование 	setting.py  >> LOGGING:dict
* разворачиваем логирование 	import logging  logger = logging.getLogger(__name__)
#
* порядок описания логирования formatters, handlers, loggers
* что куда ложится в логировании formatters в handlers, handlers в loggers
* как в приложении вызвать логгер из проекта    logger=logging.getLogger(__name__)