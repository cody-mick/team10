from django.db import models

# Create your models here.
class QuesModel(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    hint = models.CharField(max_length=400, null=True)
    point_value = models.IntegerField(max_length=7, null=False, default=0)
    
    def __str__(self):
        return self.question