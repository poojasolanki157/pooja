from django.db import models

# Create your models here.
class Bgimage(models.Model):
	bg_title=models.CharField(max_length=200)
	bg_image=models.FileField(upload_to='bgimage',blank=True)
	
	
	
	class Meta:
		verbose_name_plural='bg image'