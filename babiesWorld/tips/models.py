from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class HealthTipsForBaby(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE,
								related_name='author_detail')
	title = models.CharField(max_length=50)
	image_url = models.URLField(help_text='Link to an Image File')
	message = models.TextField()
	is_featured = models.BooleanField(default=False)
	timeStamp = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateField(auto_now=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-timeStamp']
		verbose_name = 'Health Tips'
		verbose_name_plural = 'Health Tips for Babies'
