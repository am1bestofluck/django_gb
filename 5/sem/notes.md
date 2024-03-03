# работа с административной панелью
## 1
валидаторы пароля можно выключить в settings.py проекта, там они есть по дефолту
## 2
регистрируем через декоратор:

~~~
@admin.register(ModelName)
class ModelNameAdmin(admin.ModelAdmin):
    pass

~~~
нужно убедиться что приложение из которого берём модели- подключено
## 3
кликаем в интерфейсе

имя группы отражает какие у неё права и в какой группе

в groups "+"; задаём имя; добавляем буллеты из выпадающего списка

на всякий случай сделать миграции

пользователю можно дать группу полномочий из созданных ранее и присвоить индивидуальные права

галочка staff status - позволяет пользователю авторизваться в админку
галочка active - "бан"; запрет пользоваться сайтом, без удаления аккаунта
[26:48]

# 5 

примитивный вывод: переопределение __str__
что будем делать:
    вывод списков через admin.py

@admin.register
class AuthorAdmin(admin.ModelAdmin):
    list_display= ['fields', 'from','model'] # что выводим
    list_display_links =['link_field'] # делает поле ссылкой (на update)?
    list_filter=['from'] # фильтр по полю

# 6
~~~fieldsets = (
    ('name_of_group_str',{'fields':["what we'll show","here"]}),
    ('descripted_group',{'description':"We write about group here!"}),
    ('formatted_group',{'styles':['custom','collapse']}),
    ('read_only_view',{'fields':["we can't"," edit it"],
                        'readonly_fields':["we can't"," edit it"],
    }
),
)
~~~
# offtop
model.objects.create - лучше, типа валидирует данные

дз = 5,6+суперпользователь+lg_pw_superuser

cms - content management system
django может быть асинхронным ( с 3ей версии)
будь здоров ^.^