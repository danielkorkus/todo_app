from django.urls import path
from rest_framework import routers
from .views import TodoViewSet

#run in dev as local/api/todos
router = routers.DefaultRouter()
router.register(r'api/todos', TodoViewSet, 'todos')
urlpatterns = router.urls
