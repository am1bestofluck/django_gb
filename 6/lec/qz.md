django debug toolbar(DjDT) 	инструмент отладки django-приложений
* что измеряют панели Django Debug Toolbar(7) 	запросы,шаблоны,sql-запросы, кэш, функции, http-заголовки, информацию о системе хоста
* куда выводится отчёт DjDT 	панель логирования
* устанавливаем DjDT 	pip install django-debug-toolbar
* правка settings.py для djdt(3) 	INTERNAL_IPS=['127.0.0.1']
INSTALLED_APPS=['debug_toolbar',]
MIDDLEWARE=['debug_toolbar.middleware.DebugToolbarMiddleware']
Порядок подключения djdt в settings.py[middleware] 	как можно раньше
* настраиваем urls.py для djdt 	urlpatterns=[path('__debug__/',include('debug_toolbar.urls'))]
* создаём в одном запросе несколько строк в базе из коллекции объектов 	Model.objects.bulk_create(list_of_objs)
* django импорт функции суммирования элементов бд 	from django.db.modules import Sum	
* пример суммирования элементов 	total = Product.objects.aggregate(Sum('quantity'))
* для модели; поля для числа: положительное, целое, до 32767 	models.PositiveSmallIntegerField()
# деплой, привязан к платформе pythonanywhere.com
* shareware хост python 	www.pythonanywhere.com
* что в целом нужно сделать() 	поправить настройки сервера;
подключить бд; обработать файл requirements.txt; актуализировать удалённый репозиторий и подключить его на хосте py..here;
* что добавляем в settings.py(концептуально)(6)	отключаем debug;
добавляем csrf токен;
подключаем секретный ключ;
добавляем новый хост;
подключаем бд(mysql); настраиваем сервер
* мой хост 	am1bestofluck
* правка setting.py: отключаем дебаг, добавляем хост 	DEBUG=False
ALLOWED_HOSTS = [
'127.0.0.1', ...
'{username}.pythonanywhere.com']
* правка settings.py: csrf, секретный ключ 	SESSION_COOKIE_SECURE= True
CSRF_COOKIE_SECURE = True
SECRET_KEY = os.getenv('SECRET_KEY')
[next]
* в консоли бд на сайте меняем пароль(sql запрос) 	ALTER DATABASE username$default CHARACTER SET utf8 COLLATE utf8_general_cli;
* правка settings.py для mysql 	DATABASES ={
	'default': {
		'ENGINE':'django.db.backends.mysql',
		'NAME':'<username>$<db_name>',
		'USER':'<username>',
		'PASSWORD':os.getenv('MYSQL_PASSWORD'),
		'HOST':'<mysql_hostname>',
		'OPTIONS':{
			'init_command':"SET NAMES 'utf8mb4';SET sql_mode='STRICT_TRANS_TABLES'",
			'charset':'utf8mb4',
		}, }}
* python модуль asgiref 	реализация ASGI
* python модуль sqlparse 	парсер строк в sql
* python модуль tzdata 	обрабатывает локальное время
* python модуль python-dotenv 	обрабатывает .env файлы; добавляет их пары кл-зн в систему( н. для os.environ)
* ожидаемое содержание файла requirements.txt( без версий) 	asgiref Django django-debug-toolbar Pillow sqlparse tzdata mysqlclient python-dotenv
* готовим git проект к добавлению на ресурс 	убираем медиа( /media/ /static/) и сопроводительные файлы( * .log, * .pyc * .sqlite3)
* подключаем наш проект в консоли py..here 	git clone https://github.com/<my_name>/<projectname>.git
* в консоли py..here создаём виртуальное окружение 	mkvirtualenv --python=/usr/bin/python3.10 virtualenv
* устанавливаем зависимости 	cd myproject
pip install -r requirements.txt
* создаём вебприложение 	на dashboard[web apps] > add a new web app > {select name} > manual configuration > {select python version} > {next}
* настраиваем веб-приложение( 	в настройках указываем путь до в.окружения) /home/username/ .virtualenvs/virtualenv
* редактируем wsgi.py 	раскомментируем и правим блок django( ~74-90 строки)
* генерируем секретный ключ в консоли python 	import secrets
secrets.token_hex() # exit()
* куда добавлять секрет{ные ключи} 	в папку указанную в wsgi.py[project_folder]
* добавляем секретный ключ	echo "export SECRET_key=from_secrets.token_hex()" >> .env
echo "export MYSQL_PASSWORD={dbpassword}" >> .env
* что нужно сделать чтобы применить обновления к веб-приложению 	найти и нажать кнопку обновить :]
* где искать логи ошибок 	корневая директория
* даём консоли виртуальной ОС доступ к сокрытым данным веб-приложения 	echo 'set -a; source ~/myproject.env; set +a' >> ~/.virtualenvs/virtualenv/bin/postactivate
* применяем миграции к базе данных mysql после того как консоль получила доступ к переменным окружения 	python manage.py migrate
* собираем статические файлы в одну структуру( django, внутри консоли virtualenv) 	python manage.py collectstatic
* добавляем в хост адрес настроенной статики django 	web > static files > [URL === /static/ ; Directory === { сообщает django как результат python manage.py collectstatic}]
* создаём суперпользователя для администрирования НАШЕГО сайта в облаке(консоль venv)	python manage.py createsuperuser