from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task
from .serializer import TaskSerializer
from drf_spectacular.utils import extend_schema


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.active()
    serializer_class = TaskSerializer


    
    def get_queryset(self):
        if self.action == 'restore':
            # Se a ação for 'restore', retorna apenas as tarefas deletadas
            return Task.objects.filter(is_deleted=True)
        return Task.objects.active()
    
    @extend_schema(
        operation_id="Restaura uma tarefa marcada como deletada.",
        description="Restaura uma tarefa marcada como deletada.",
        tags=['Soft Delete'],
        responses={
            200: TaskSerializer,
            404: "Tarefa não encontrada.",
        }
    )
    @action(detail=True, methods=['post'], url_path='restore')
    def restore(self, request, pk=None):
        """Restaura uma tarefa marcada como deletada."""
        task = self.get_object()
        task.restore()
        serializer = self.get_serializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    

    @extend_schema(
        operation_id="Lista todas as tarefas que foram marcadas como deletadas.",
        description="Lista todas as tarefas que foram marcadas como deletadas.",
        tags=['Soft Delete'],
        responses={
            200: TaskSerializer(many=True),
        }
    )
    @action(detail=False, methods=['get'], url_path='deleted')
    def list_deleted(self, request):
        """Lista todas as tarefas que foram marcadas como deletadas."""
        deleted_tasks = Task.objects.filter(is_deleted=True)
        serializer = self.get_serializer(deleted_tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)