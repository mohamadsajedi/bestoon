from django.urls import path
from . import views

urlpatterns = [
    path('submit/expense/', views.submit_expense, name='submit_expense'),
    path('register/', views.register, name='register'),
    path('', views.index, name='index'),
    path('logout/', views.logout, name='logout')
]