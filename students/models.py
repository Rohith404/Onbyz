from django.db import models

class Students(models.Model):
	Name = models.CharField(max_length = 100)
	Class = models.CharField(max_length = 100)
	Subject = models.CharField(max_length = 100)
	Year_And_Month = models.DateField()
	Image = models.ImageField(upload_to = 'Images')

	def __str__(self):
		return self.Name