from django.db import models
from autoslug import AutoSlugField
from djmoney.models.fields import MoneyField
from django.core.validators import MinValueValidator, MaxValueValidator


class BabyCareCategory(models.Model):
	name = models.CharField(max_length=25)
	slug = AutoSlugField(populate_from='name', always_update=False)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']
		verbose_name_plural = 'Baby Care Categories'


class BabyCare(models.Model):

	PAY_INTERVAL = (
		('Daily', 'Daily'),
		('Weekly', 'Weekly'),
		('Monthly', 'Monthly'),
		('Quarterly', 'Quarterly'),
		('Bi Annually', 'Bi Annually'),
		('Annually', 'Annually')
	)

	GENDER = (
		('Male', 'Male'),
		('Female', 'Female')
	)

	care = models.ForeignKey(BabyCareCategory, on_delete=models.DO_NOTHING, null=True,
							related_name='baby_care')
	title = models.CharField(max_length=20)
	agent_full_name = models.CharField(max_length=150)
	slug = AutoSlugField(populate_from='agent_full_name', always_update=False)
	salary = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
	pay_interval = models.CharField(max_length=11, choices=PAY_INTERVAL)
	gender = models.CharField(max_length=6, choices=GENDER)
	date_of_birth = models.DateField(null=True, blank=True)
	age = models.PositiveIntegerField(validators=[
									MinValueValidator(18),
									MaxValueValidator(60)
									])
	agent_description = models.TextField()
	image = models.ImageField(upload_to='care', default='/care/And still I rise.jpeg')
	ratings = models.IntegerField(null=True, blank=True, validators=[
									MinValueValidator(1),
									MaxValueValidator(5)
									])
	firm = models.CharField(max_length=200, help_text='Could be name of Firm, Day care etc..')
	firm_contact = models.CharField(max_length=50)

	def __str__(self):
		return self.agent_full_name

	class Meta:
		ordering = ['agent_full_name']
		verbose_name_plural = 'Babies Care'


class BabyHealth(models.Model):
	title = models.CharField(max_length=20)
	full_name = models.CharField(max_length=150)
	slug = AutoSlugField(populate_from='full_name', always_update=False)
	gender = models.CharField(max_length=6, choices=BabyCare.GENDER)
	date_of_birth = models.DateField(null=True, blank=True)
	age = models.PositiveIntegerField(validators=[
									MinValueValidator(18),
									MaxValueValidator(60)
									])
	physician_description = models.TextField()
	image = models.ImageField(upload_to='physician', default='/physician/And still I rise.jpeg')
	ratings = models.IntegerField(null=True, blank=True, validators=[
									MinValueValidator(1),
									MaxValueValidator(5)
									])
	clinic = models.CharField(max_length=200, help_text='Could be name of Clinic or Hospital')
	clinic_contact = models.CharField(max_length=50)

	def __str__(self):
		return self.full_name

	class Meta:
		ordering = ['full_name']
		verbose_name_plural = 'Babies Health'
