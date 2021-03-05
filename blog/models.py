from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=200)
	image = models.ImageField(upload_to='blog/images/')
	pub_date =models.DateField(auto_now=False, auto_now_add=False)
	name = models.CharField(max_length=30)
	body = models.TextField(max_length=2000, help_text='Enter a brief description of the course')
	def __str__(self):
		return self.title

		def Summary(self):
			return self.body[:100]
 