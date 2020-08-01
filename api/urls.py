
from django.urls import path
from . import views

urlpatterns = [
    path('', views.apioverview, name='api-overview'),
    path('all-hackers/',views.allhackers,name='all-hackers'),
    path('add-hacker',views.hackerAdd,name='add-hacker'),
    path('hacker-update/<str:pk>',views.hackerUpdate,name='hacker-update'),
    path('hacker-delete',views.hackerDelete,name='hacker-delete'),
]
