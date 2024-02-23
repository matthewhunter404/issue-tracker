from django.db import models

class Issue(models.Model):
    issue_text = models.CharField(max_length=200)
    completion_state = models.BooleanField(default=False)
    creation_date = models.DateTimeField("date created")
    def __str__(self):
        return self.issue_text

class Comment(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    creation_date = models.DateTimeField("date created")
    def __str__(self):
        return self.comment_text