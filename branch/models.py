from django.db import models

# Create your models here.

class Branch(models.Model):
	#pass
	#id_number=models.IntegerField(default=1)
	branch_name=models.CharField(default='Any branch',max_length=500)
