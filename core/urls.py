from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name='register'),
    path('update_password/', views.update_password, name='update_password'),
    path('update_user/', views.update_user, name='update_user'),
    # path('update_info/', views.update_info, name='update_info'),
    path('information/', views.texts, name='information'),
    path('informations/', views.allTexts, name='informations'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('download/', views.download_csv, name='download_csv'),
]
