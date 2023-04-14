from django.urls import path
from . import views
from .views import BrickListView, BrickDetailView, SetListView, SetDetailView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # /
    path('', views.index, name='index'),

    # /filter/
    path('filter/', views.finder, name='filter'),

    # /help/
    path('docs/', views.docs, name='docs'),

    # /my_bricks/
    path('collection', views.collection, name='collection'),

    # /bricks/
    path('bricks/', BrickListView.as_view(), name='brick_list'),
    path('bricks/<int:pk>/', BrickDetailView.as_view(), name='brick_detail'),

    # /sets/
    path('sets/', SetListView.as_view(), name='sets'),
    path('sets/<int:pk>/', SetDetailView.as_view(), name='set_detail'),
    path('filter/run', views.filter_collection, name='filter_run'),

    path('bricks/add/<int:brick_id>', views.add_brick, name='add_brick'),
    path('bricks/del/<int:brick_id>', views.del_brick, name='del_brick'),
    path('set/add/<int:id>/', views.add_set, name='add_set'),
    path('set/del/<int:id>', views.del_set, name='del_set'),
    path('set/convert/<int:id>', views.convert, name='convert'),

    # Account management
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('logout/', views.logout, name='logout'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'), 
]