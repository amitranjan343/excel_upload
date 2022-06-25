from django.db import models

class Excel_DB(models.Model):
    fname = models.CharField(max_length=50)
    data = models.JSONField(null=True)
