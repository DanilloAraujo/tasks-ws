from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from crud_ws.apps.tasks.models import Task
from crud_ws.apps.tasks.serializer import TaskSerializer
from crud_ws.apps.utils.pagination import StandardResultsSetPagination


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, )

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(owner=request.user)
        return super().list(request, *args, **kwargs)
