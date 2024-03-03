import pdb
from datetime import date
from typing import Union, List
from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, View, FormView, CreateView

# import models
from .models import Author, Article, Comment
from . import forms


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
        # pdb.set_trace()
        art_id = kwargs['article_id']
        article = get_object_or_404(Article, pk=art_id)
        context['title']: str = f"Comments on '{article.title}'"
        context['details'] = dict()
        context['details']['title']: str = article.title
        context['details']['content']: str = article.content
        context['comments']: QuerySet[Comment] = Comment.objects.filter(article_id__exact=art_id)

        # pdb.set_trace()
        return context


# def new_author(request):
#     # pdb.set_trace()
#     if request.method == "POST":
#         form = forms.Author_form(request.POST)
#         pdb.set_trace()
#         if form.is_valid():
#             form.save()
#         return redirect("new_author")
#     else:
#         form = forms.Author_form()
#         return render(request, "blog_models/author_form.html", {"form": form})


class NewAuthorView(View):
    def get(self, request):
        form = forms.Author_form()
        return render(request, "blog_models/author_form.html", {"form": form})

    def post(self, request):
        form = forms.Author_form(request.POST)
        pdb.set_trace()
        if form.is_valid():
            form.save()
        return redirect("new_author")


class NewArticleView(GetAllCommentsOnArticle):
    def get(self, request):
        form = forms.Article_form()
        return render(request, "blog_models/author_form.html", {"form": form})

    def post(self, request):
        form = forms.Article_form(request.POST)
        try:
            form.is_valid()
        except:
            pdb.set_trace(header="почему??? почему здесь author это None!!!")
        if form.is_valid():
            new_article: Article = Article(title=form.cleaned_data['title'],
                                           content=form.cleaned_data['content'],
                                           publication_date=form.cleaned_data['publication_date'],
                                           author=Author.objects.get(pk=int(form.data['author'])),
                                           tags=form.cleaned_data['tags'],
                                           isPublished=form.cleaned_data['isPublished'])
            new_article.save()
            return redirect("new_article")
        else:
            return HttpResponse(form.errors)


class GetAllCommentsOnArticle_withAppend(GetAllCommentsOnArticle):
    template_name = "blog_models/all_comments_interactive.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.Comment_form()
        # pdb.set_trace()
        return context

    def post(self, request, article_id):
        form = forms.Comment_form(request.POST)
        # pdb.set_trace()
        if form.is_valid():
            new_comment = Comment(
                author=Author.objects.get(pk=form.cleaned_data['author']),
                article=Article.objects.get(pk=article_id),
                content=form.cleaned_data['content'],
                date_created=date.today(),
                date_edited=None)
            new_comment.save()
        else:
            print(form.errors)
        # pdb.set_trace()
        return redirect(f"new_comment", article_id=article_id)


# class EditWare(View):
#     template_name = "blog_models/edit_ware.html"
#
#     def get(self, request, ware_id):
#         ware = models.Ware.objects.get(pk=ware_id)
#         context = {f"verbose_title": "RW of  {ware}"}
#         context['form'] = forms.Ware_form()
#         context['ware_descr'] = ware
#         return render(request, self.template_name, context=context)
#
#     def put(self, request, ware_id):
#         form = forms.Ware_form(request.PUT)
#         if form.is_valid():
#             pdb.set_trace()
#         else:
#             return HttpResponse(form.errors)
#         return redirect("r_u_ware", ware_id=ware_id)
