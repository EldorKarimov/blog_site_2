from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogHome.as_view(), name = 'home'),
    path('category/<slug:slug>', CategoryBlog.as_view(), name = 'category'),
    path('tags/<slug:slug>', TagBlog.as_view(), name = 'tag_blog'),
    path('detail/<slug:slug>', BlogDetail.as_view(), name = 'blog_detail'),
    path('blog-creating', BlogCreate.as_view(), name = 'blog_create'),
    path('delete/<slug:slug>/', BlogDelete.as_view(), name = 'blog_delete'),
    path('categories/', CategoryBLogList.as_view(), name = 'categories'),
    path('comment-delete/<int:pk>', CommentDelete.as_view(), name = 'comment_delete'),
    path('category-add-user/<slug:slug>', CategoryAddUser.as_view(), name = 'category_add_user'),
    path('blog-update/<slug:slug>', BlogUpdate.as_view(), name = 'blog_update'),
]