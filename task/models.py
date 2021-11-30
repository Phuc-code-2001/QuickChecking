from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Task(models.Model):
    owner           = models.ForeignKey(User, on_delete=models.CASCADE)
    key             = models.CharField(max_length=24)
    name            = models.CharField(max_length=100)
    password        = models.CharField(max_length=24)
    date_of_created = models.DateTimeField(default=datetime.datetime.now())
    date_opening    = models.DateField(default=datetime.datetime.now())
    start_time      = models.TimeField(default=datetime.datetime.now().time())
    end_time        = models.TimeField(default=datetime.datetime.now().time())

    def __str__(self):
        return self.name

    def short_name(self):
        return self.name[:min(100, len(self.name))]


class Check(models.Model):
    task            = models.ForeignKey(Task, on_delete=models.CASCADE)
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    time_checked    = models.DateTimeField(default=datetime.datetime.now())


    def __str__(self):
        return f"[{self.user}] - [{self.task.id}] - [{self.time_checked.strftime(r'%Y-%m-%d %H:%M')}]"