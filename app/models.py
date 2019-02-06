from django.db import models

class Document(models.Model):
	first_name = models.CharField(max_length = 100)
	last_name = models.CharField(max_length = 100)
	pass_id = models.CharField(max_length = 10)
	phone_number = models.CharField(max_length= 11)
	def __str__(self):
		return self.last_name