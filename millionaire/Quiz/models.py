from django.db import models
from sqlalchemy import null

# Create your models here.
class QuesModel(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    hint = models.CharField(max_length=400, null=True)
    point_value = models.IntegerField(null=False, default=0)
    timer = models.IntegerField(null=True)
    
    def __str__(self):
        return self.question
    
class Scores(models.Model):
    score = models.IntegerField(null=False, default=0)
    
    def __str__(self):
        return self.score