from django.contrib import admin
from .models import Author, Comment, Article


# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass
