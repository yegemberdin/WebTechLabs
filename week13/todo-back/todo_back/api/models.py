from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class TasklistManager(models.Manager):
    def for_user_order_by_name(self, user):
        return self.filter(created_by=user).order_by('name')

    # def get_today(self, date):
    #     return self.filter(created_at.year=data.year,
    #                     created_at.month = data.month,
    #                     created_at.day = data.day)

class TaskList(models.Model):
    name = models.CharField(max_length=100)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=all)

    def to_json(self):
        return{
            'id': self.id,
            'name': self.name,
        }

class Task(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField()
    due_on = models.DateField()
    status = models.CharField(max_length=100)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    def to_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at,
            'due_on': self.due_on,
            'status': self.status,
        }