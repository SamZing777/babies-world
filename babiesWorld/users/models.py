from django.db import models
from django.contrib.auth.models import AbstractUser
from autoslug import AutoSlugField


class User(AbstractUser):
	slug = AutoSlugField(populate_from='username', always_update=False)
	pass

	def __str__(self):
		return self.username
