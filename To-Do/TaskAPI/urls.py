# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'task', TaskViewSet)

urlpatterns = [
    path('', TaskViewSet.as_view({'get': 'list'})),
    path('task-list/', TaskViewSet.as_view({'get': 'list'}), name='task-list'),
    path('task-detail/<str:pk>/', TaskViewSet.as_view({'get': 'retrieve'}), name='task-detail'),
    path('task-create/', TaskViewSet.as_view({'post': 'create'}), name='task-create'),
    path('task-update/<str:pk>/', TaskViewSet.as_view({'put': 'update'}), name='task-update'),
    path('task-delete/<str:pk>/', TaskViewSet.as_view({'delete': 'destroy'}), name='task-delete'),
    path('my-api', include(router.urls)),  
]
