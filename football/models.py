from django.db import models

# Create your models here.
class Category(models.Model):

	#str Helper method to return the title if we list out
	def __str__(self):
		return self.title

	title = models.TextField(max_length=200)


class Article(models.Model):
	title = models.TextField(max_length=200)
	author = models.TextField('Author', max_length=200)
	publishedAt = models.DateTimeField('Date Published')
	category = models.ForeignKey(
    'Category',
    on_delete=models.CASCADE,
)	#foreign key
	description = models.TextField()
	hero_image = models.TextField('Hero Image')
	additional_image = models.TextField('Additonal Image', null=True, blank=True)

	#str Helper method to return the title if we list out
	def __str__(self):
		return self.title