from django.db import models
# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    completion_state = models.BooleanField(default=False)
    creation_date = models.DateTimeField("date created")
    def __str__(self):
        return self.project_name