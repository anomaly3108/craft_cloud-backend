from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('type/', views.show_type, name='show_type'),
    path('users/<uid>', views.users, name='users'),
    path('top_users', views.top_users, name='top_users'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('posts/<type>', views.user_post, name='user_post'),
    path('addpost/', views.add_post, name='add_post'),
    path('user_rating/<uid>', views.ratings, name='user_rating'),
    path('ratings_update/<uid>', views.ratings_update, name='user_rating_update'),
    path('user_details/<uid>', views.user_details, name='user_details'),
    path('single_post/<pid>', views.single_post, name='single_post'),
    path('cart/<uid>', views.show_cart, name='cart'),
    path('add_cart', views.add_cart, name='add_cart'),
    path('get_orders/<pid>', views.get_orders, name='get_orders'),
    path('add_orders', views.add_orders, name='add_orders'),
    path('wallet/<uid>', views.view_wallet, name='view_wallet'),

]
