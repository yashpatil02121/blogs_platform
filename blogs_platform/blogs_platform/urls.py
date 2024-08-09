from django.contrib import admin
from django.urls import path
from users import views as user_views
from posts import views as post_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', user_views.Registration, name="registration"),
    path('login/', user_views.Login, name="login"),
    path('logout/', user_views.Logout, name="logout"),
    path('home/', user_views.Home, name="home"),

    path('', post_views.post_list, name='post_list'),
    path('post/<int:pk>/', post_views.post_detail, name='post_detail'),
    path('post/new/', post_views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', post_views.post_update, name='post_update'),
    path('post/<int:pk>/delete/', post_views.post_delete, name='post_delete'),
]
    