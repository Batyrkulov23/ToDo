from django.db import models
from django.utils.timezone import now

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField(default=now)  # Автоматически добавляется текущая дата и время
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
