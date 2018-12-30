from django.db import models
from django.contrib import admin

class Author(models.Model):
	name = models.CharField(max_length=64)
	email = models.CharField(max_length=64)

	def __str__(self):
		return "%s (%s)" % (self.name, self.email)

class Post(models.Model):
	title = models.CharField(max_length=64)
	image = models.ImageField(upload_to='static/')
	date = models.DateTimeField()
	author = models.ForeignKey(
		Author,
		on_delete=models.CASCADE,
	)
	body = models.TextField()

	def __str__(self):
		return "%s (%s)" % (self.title, self.author.name)
