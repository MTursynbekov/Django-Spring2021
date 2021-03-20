from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import TODOList, Task
from .serializers import TODOListSerializer, TaskSerializer, TODOSerializer


class TODOListViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        if self.action == 'create':
            return Task.objects.all()
        return TODOList.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return TaskSerializer
        elif self.action == 'list':
            return TODOListSerializer
        return TODOSerializer

    @action(methods=['get'], detail=True)
    def completed(self, request, *args, **kwargs):
        serializer = TODOSerializer(self.get_queryset().filter(id=kwargs['pk']),
                                    many=True,
                                    context={"completed": True})
        return Response(serializer.data)
