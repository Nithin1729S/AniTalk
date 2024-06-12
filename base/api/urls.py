from django.urls import path
from . import views

urlpatterns=[
    path('',views.getRoutes),
    path('forums/',views.getForums),
    path('forums/<str:pk>',views.getForum),
    path('topics/',views.getTopics),
    path('topics/<str:pk>',views.getTopic),
    path('users/',views.getUsers),
    path('users/<str:pk>',views.getUser),
    path('messages/',views.getMessages),
    path('messages/<str:pk>',views.getMessage),
]