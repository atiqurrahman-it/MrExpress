from django.urls import path
from accounts import views

app_name = "accounts"
urlpatterns = [
    path('register/', views.Register, name='register'),
    path('login/', views.Login, name='login'),
    path('logout/', views.LogOUt, name='logout'),
    path('activate/<uid>/<token>/', views.activate, name="activate"),  # login when email verification  link



]
