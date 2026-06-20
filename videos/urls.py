from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.login_view, name='login'),
    path('home', views.home, name='home'),

    path('upload/', views.upload_video, name='upload_video'),
    path('video/<int:pk>/', views.video_detail, name='video_detail'),
    path('logout/', views.logout_view, name='logout'),
    path('manage/', views.video_manager, name='video_manager'),
    path('delete/<int:video_id>/', views.delete_video, name='delete_video'),
    path('register/', views.register_view, name='register'),



    
]

