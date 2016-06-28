from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class BlogPost(models.Model):
	# Get the user that posted this
	author = models.ForeignKey('auth.User')
	# The title of the blog, given a max length of 100
	title = models.CharField(max_length=100)
	# The publication date
	pub_date = models.DateTimeField('Date Published')
	# Giving the possibility to upvote the blog post
	votes = models.IntegerField(default=0)
	# The content of the blog post
	content = models.TextField()

	def __str__(self):
		# Makes it easier to read in the shell
		return self.title

	def get_detail_link(self):
        # Returns the detail link for the blog post
		return "/{0}/".format(self.id)

	def get_date_and_author(self):
		# Returns the date and the author for the blog post
		return "Posted {0} by {1}".format(self.pub_date, self.author)
