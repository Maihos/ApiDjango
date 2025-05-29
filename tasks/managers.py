from django.db import models
class TaskQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_deleted=False)
    
