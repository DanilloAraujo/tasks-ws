from rest_framework.routers import DefaultRouter

from crud_ws.apps.accounts.api import UserViewSet
from crud_ws.apps.tasks.api import TaskViewSet

router = DefaultRouter()
router.register(r'v1/users', UserViewSet)
router.register(r'v1/tasks', TaskViewSet)
