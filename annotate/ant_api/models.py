from django.db import models

class AntDoc(models.Model):
    document = models.CharField(max_length = 2000)

