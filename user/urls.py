from django.urls import path
from user import views
from django.contrib.auth import views as auth_views
# from django.urls import url 

app_name="user"
urlpatterns=[
    
path("register/",views.signup,name="register"),
path("login/",views.login_page,name="login"),
path("list/",views.Userview,name="list"),
path("post_data/",views.post_Userdata,name="post"),
path("<int:id>/",views.post_userdetail,name="user_detail"),


    #reset-password urls
path("accounts/password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
path("accounts/password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
path("accounts/reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
path("accounts/reset/done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

]

