import pdb

from django.contrib import admin
from .models import Author, Comment, Article


# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    # pdb.set_trace()
    list_display = [i.name for i in Author._meta.fields]
    list_display.remove('bio')
    list_display_links = ['email']
    readonly_fields = ['full_name']
    fieldsets = (('for full_name', {'fields': ['full_name','email'], 'classes': ['collapse'],
                                    'description': "That's hot and all, BUT WHERE DO I READ DOCS?"}),)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [i.name for i in Comment._meta.fields]
    list_display.remove('content')
    readonly_fields = ['author', 'article']
    fieldsets = (
        ('descriptors', {'fields': ['author', 'article'], }),
        ('text', {'fields': ['content'], 'classes': ['collapse']}))


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [i.name for i in Article._meta.fields]
    list_display.remove('content')
    readonly_fields = ['id', 'author']
    fieldsets = (('support', {'fields': ['id', 'author']}), ('content', {'fields': ['content']}),)
