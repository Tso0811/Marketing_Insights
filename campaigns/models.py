from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Campaigns(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField() #活動日期(不含時間)
    budget = models.IntegerField()
    click = models.IntegerField(default=0)

    poster = models.ForeignKey(User , on_delete=models.CASCADE)
    def __str__(self):
        return (self.name)
    
    class Meta :
        verbose_name = 'Campaign'
        verbose_name_plural = 'Campaigns'