import pdb
from typing import Union, List
from django.db.models import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Author, Article, Comment


# Create your views here.

class GetArticleHeaders(TemplateView):
    # проверять будем на авторе 5, там есть публичные и приватные
    template_name = "blog_models/all_headers.html"

    def get_context_data(self, **kwargs):
        aid = kwargs['author_id']
        context = super().get_context_data(**kwargs)
        context['title'] = f'Get all article titles of {Author.objects.filter(id=aid).first().full_name}'
        context['articles'] = Article.objects.filter(author_id__exact=aid)
        # pdb.set_trace()
        return context


def get_article_with_views_increment(request, **kwargs):
    aid = kwargs['article_id']
    article = get_object_or_404(Article, pk=aid)
    author = Author.objects.filter(id=article.author.pk).first()
    context = {"title": f"Get info on '{article.title}' of {author.full_name}"}
    context.update({"details": article})
    article.views += 1
    article.save()
    # pdb.set_trace()
    return render(request, "blog_models/all_articles.html", {"context": context})


class GetAllCommentsOnArticle(TemplateView):
    template_name = "blog_models/all_comments.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pdb.set_trace()
        art_id = kwargs['article_id']
        article = get_object_or_404(Article,pk=art_id)
        context['title']: str = f"Comments on '{article.title}'"
        context['details'] = dict()
        context['details']['title']: str = article.title
        context['details']['content']: str = article.content
        context['comment']: QuerySet[Comment] = Comment.objects.filter(article_id__exact=art_id)

        pdb.set_trace()
        return context
