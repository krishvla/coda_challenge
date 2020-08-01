from django.urls import path
from . import views

urlpatterns = [
    # path('', views.apioverview, name='api-overview'),
    # path('all-tasks/',views.allTasks,name='all-tasks'),
    # path('task-detail/<str:pk>',views.taskDetail,name='task-detail'),
    # path('task-create',views.taskCreate,name='task-create'),
    # path('task-update/<str:pk>',views.taskUpdate,name='task-update'),
    # path('task-delete/<str:pk>',views.taskDelete,name='task-delete'),
    path('',views.homeview,name='home'),
    path('login/',views.loginview,name='login')
]