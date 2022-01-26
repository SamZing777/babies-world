from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from autoslug import AutoSlugField


class User(AbstractUser):
	slug = AutoSlugField(populate_from='username', always_update=False)
	pass

	def __str__(self):
		return self.username

	def get_absolute_url(self):
		return reverse('user-detail', args=[str(self.id)])
