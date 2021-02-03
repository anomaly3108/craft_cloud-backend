from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', views.show, name='show'),
    path('users/<uid>', views.users, name='users'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('posts/', views.user_post, name='user_post'),
    path('addpost/', views.add_post, name='add_post'),
    path('user_details/<uid>', views.user_details, name='user_details')
]
