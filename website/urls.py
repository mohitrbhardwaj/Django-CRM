from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    # path('login/', views.login_user, name = 'login'),
    path('logout/', views.logout_user, name = 'logout'),
    path('signup/', views.signup_user, name = 'signup'),
    path('record/<int:pk>', views.user_record, name = 'record'),
    path('delete_record/<int:pk>', views.delete_record, name = 'delete_record'),
]
