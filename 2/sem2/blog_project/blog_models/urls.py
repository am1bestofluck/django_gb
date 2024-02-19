from django.urls import path
# from .models import Author, Article
from . import views

urlpatterns = [
    path('all_headers/<int:author_id>', views.GetArticleHeaders.as_view(), name='headers_by_id'),
    path('all_articles/<int:article_id>', views.get_article_with_views_increment, name='get_article'),
    path('all_comments/<int:article_id>', views.GetAllCommentsOnArticle.as_view(), name='get_comments')
]
