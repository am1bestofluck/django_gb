# работа с административной панелью
* роль административной панели(2)	управление данными; инструмент администрирования приложения
* меняем язык админки 	в проектном setting.py меняем LANGUAGE_CODE{ = "ru-ru"}
* создаём суперпользователя 	python manage.py createsuperuser
* сбрасываем пароль... :D 	python manage.py changepassword <username>
* интерфейс таблицы пользователей в админке 	crud реализован по умолчанию
* выходим с админки(сслыка) 	<host>/admin/logout
* как добавляем в административную панель модель из приложения(концепт) 	редактируем admin.py приложения
* пример добавления модели в админку(admin.py) 	from django.contrib import admin
from .models import Mdl
admin.site.register(Mdl)
* создаём дочерний объект для представления объектов в админке 	class ViewForAdmin(admin.ModelAdmin):
  list_display=['names','of','fields']
* сортировка вывода для админского view 	ordering=['names_of','-fields']
* что означает - в ordering 	обратная сортировка по этому полю
* добавление фильтра в админский view 	list_filter=['names_of','fields']
* оформляем поиск в админском view 	searh_fields=['name_of_field']
search_help_text= "Поиск по name_of_field"
* декоратор для добавления новых команд 	@admin.action(description="ui label for function")
* пример новой команды 	@admin.action(description="del stuff")
  def reset_quantity(modeladmin,request,queryset):
    queryset.{update(key_qua=0)}
* добавляем новую команду в админское view 	actions=reset_quantity # без кавычек!
* меняем представление экземпляров модели(2) 	fields=["read_post", "this"]
readonly_fields = ['read','this']
* синергия readonly_fields из админского представления и автогенерируемых полей в модели 	поля заполняемые по сценарию нужно делать read_only, или выдаст ошибку