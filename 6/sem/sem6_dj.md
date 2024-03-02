оптимизация sql запросов 	извлекаем не все поля а только часть
 
Алгоритм:
в settings csrf session cookie
[20]
#
создаём .env
ложим туда SECRET_KEY='from secrets.token_hex()'
DEBUG = 'False'
MYSQL_DBNAME=''
MYSQL_USER=''
MYSQL_PASSWORD=''
MYSQL_HOST=''
#
pip install python-dotenv
pip install mysql-client
#
#settings.py
from dotenv import load_dotenv
load_dotenv() # над BASE_DIR, под импортами
#заменяем переменные-литералы на то что в .env
SECRET_KEY=os.getenv('SECRET_KEY')
DEBUG=os.getenv('DEBUG')
#debug toolbar отключаем если есть
## переходим на pythonanywhere
сверху databases
*предлагает создать пароль; создаём отличный от учётки*
выводит username и host; копируем это, вставляем в .env
ниже yourdatabases>name: copypaste(.env,name)
## продолжаем редактировать settings.py
#меняем DATABASES
DATABASES= {
	"default": {
		"ENGINE":'django.db.backends.mysql',
		"NAME":os.getenv("MYSQL_NAME"),
		"USER":os.getenv("MYSQL_USER"),
		"PASSWORD":os.geten v("MYSQL_PASSWORD"),
		"HOST":os.getenv("MYSQL_HOST"),
		"OPTIONS":{
			"init_command":"SET NAMES 'utf8mb4'; SET sqlite_mode = 'STRICT_TRANS_TABLES'",
			"charset":"utf8mb4",
			},
		
	}
}
#settings.py[ALLOWED_HOSTS]+='am1bestofluck.pythonanywhere.com'
##
csrf, cookie в рамках методички
##
смотрим static,media пути
##
settings - media отключаем или заворачиваем в if
##
открываем на сайте консоль бд(кликаем на имя базы данных)
вводим там:
ALTER DATABASE username$default CHARACTER SER utf8 COLLATE utf8_general_cli;
exit

#
создаём зависимости, там где manage.py
pip freeze > requirements.txt

### идеал проекта: файл env, файл requirements, файл manage
#наводим порядок в репозитории и пушим

#на гитхабе копируем адрес репозитория (из кнопки)
#на py..ere dashboard>new_console>$bash  git clone <>
#делам виртуальное окружение python3 -m venv venv
*пока делается окружение*
на сайте py..ere делаем новое приложение: web>add new web app> manual>python3.10>>
virtualenv:
*enterpathtovenvifdesired*>/home/<username>/<reponame:fromgithub>/venv
*установилось окружение, возвращаемся в консоль*
#source venv/bin/activate
#pip install -r requirements.txt
*пока устанавливается - идём на сайт*
там где указывали путь venv ищем code:
>> wsgi config.file>
###удаляем всё что ниже и выше блока django
###раскомментируем, то что выглядит как код  python
###дописываем:
~~~
from dotenv import load_dotenv
project_folder = os.path.expanduser('~/<projectname:directory_folder>')
load_dotenv(os.path.join(project_folder,'.env'))
# правим строку path=
path='/home/<username>/<projectfolder>'
# правим строку os.environ['DJANGO_SETTINGS_MODULE']='<projectNAME:manage.py root folder>.settings'
~~~
жмём save (wsgi)
<<<
##возвращаемся в консоль bash
*mysqlclient* - одним словом
python manage.py migrate
*возвращаемся на сайт*
static files:
urls>/static/
directory> /home/<username>/<projectname>/static/ # python manage.py collectstatic даст этот путь
там же одной строкой ниже повторяем для media
*если проблемы - можно у нас сделать изменения, сделать пуш у нас и пул там*
##создаём суперпользователя python manage.py createsuperuser
##python manage.py collectstatic

**ошибка, csrf cookie not set**
https://stackoverflow.com/questions/17716624/django-csrf-cookie-not-set
они решили через отключение в настройках 
**фиск картинок**
путь к картинкам MEDIA_URL="/media/"
в шаблоне: <img src="/media/{{ pr.image }}" alt = "no pic">
совет от методиста:
<img src="{{ pr.image.url }}">
-картинки показывает просто как ссылку на поле {{ pr.media }}-
хмммм.
Дз: развернуть магазин; ссылку на сайт; ссылка на репозиторий; реквизиты админки; немного скринов рабочего приложения НА ВСЯКИЙ СЛУЧАЙ