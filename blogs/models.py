from django.db import models

# Create your models here.
class Blog(models.Model):
	"""docstring for Blog_Model"""
	genre_type = [
		("Science and Technology","Science and Technology"),
		("Literature","Literature"),
		("Action","Action"),
		("Personal Expierence","Personal Expierence"),
	]
	author = models.CharField(max_length=30)
	title  = models.CharField(max_length=30)
	genre  = models.CharField(max_length = 30, blank = True, null = True, choices=genre_type)
	content= models.TextField(blank = False)
	date   = models.DateField(blank= False, auto_now=True)

	def __str__(self):
		return str(self.pk)+" "+ str(self.date)

		

	
