from django.urls import path
from blog_api import views
from django.contrib.auth import views as auth_views
app_name="blog_api"
urlpatterns=[
path("login/",views.login_user,name="login"),
path("logout/",views.logout_user,name="logout"),
path("create/",views.article_create,name="create"),
path("<int:id>/",views.article_detail,name="detail"),
path("user/<int:id>/",views.article_list,name="list"),
path("comment/<int:id>/",views.article_comment_and_like_list,name="comment_list"),
]