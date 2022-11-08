from django.urls import path
from myblog import views


app_name = "myblog"

urlpatterns = [
    path("", views.home_view, name="home"),
    # path("",views.list_view,name="home"),
    path("list",views.list_view,name="list"),
    # path('<slug:slug>/',views.detail_view,name="detail"),
    path("<int:aid>/",views.detail_view,name="detail"),
    path("create",views.create_view,name="create"),
    # path('like/',views.user_like_post,name="user_like_post"),
    path('like/',views.like_post,name="like-post"),
    path('contact',views.contact_view,name="contact"),

    
    
]