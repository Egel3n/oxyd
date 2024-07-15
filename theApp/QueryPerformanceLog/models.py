from django.db import models

# Create your models here.
class QueryPerformanceLog(models.Model):
    EventDate = models.DateTimeField()
    DatabaseID = models.IntegerField()
    Hostname = models.CharField(max_length=30)
    AppName = models.CharField(max_length=30)
    SessionID = models.IntegerField()
    UserName = models.CharField(max_length=30)
    SqlText = models.CharField(max_length=30)
    Duration = models.IntegerField() 
    