from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerPage, name="register"),
    path('', views.home, name="home"),
    path('room/<str:pk>', views.room, name="room"),
    path('createRoom/', views.createRoom, name="create-room"),
    path('updateRoom/<str:pk>/', views.updateRoom, name="update-room"),
    path('deleteRoom/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('deletemessage/<str:pk>/', views.deleteMessage, name="delete-comment"),
    path('profile/<str:pk>', views.userProfile, name="profile-page"),
    path('update-user/', views.updateUser, name="update-user"),
    path('topics/', views.topicsPage, name="topics"),
    path('activity/', views.activityPage, name="activity"),
]
