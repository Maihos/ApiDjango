# ApiDjango/tasks/models.py

from django.db import models
from .managers import TaskQuerySet 

class SoftDeleteMixin(models.Model):
    is_deleted = models.BooleanField(default=False)

    def delete(self, using=None, keep_parents=False, soft_delete=True):
        """Sobrescreve o método delete para implementar soft delete."""
        if soft_delete:
            self.is_deleted = True
            self.save()
        else:
            super().delete(using, keep_parents)
    

    def restore(self):
        """Restaura um registro marcado como deletado."""
        self.is_deleted = False
        self.save()

    class Meta:
        abstract = True  # Esta classe não será criada como uma tabela no banco de dados


class Task(SoftDeleteMixin):  # Definindo a classe Task que herda de SoftDeleteMixin
    title = models.CharField(max_length=200)  # Campo para título da tarefa
    description = models.TextField(blank=True, null=True)  # Campo para descrição da tarefa
    completed = models.BooleanField(default=False)  # Campo para indicar se a tarefa foi concluída
    created_at = models.DateTimeField(auto_now_add=True)  # Data de criação do registro
    updated_at = models.DateTimeField(auto_now=True)  # Data de atualização do registro

    objects = TaskQuerySet.as_manager()  # Usando o TaskQuerySet para gerenciar as tarefas

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']  # Ordenação padrão







