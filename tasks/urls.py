from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, LabelViewSet, TaskViewSet, CommentViewSet


router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'labels', LabelViewSet, basename='label')
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]
