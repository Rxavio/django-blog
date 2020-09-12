from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from PIL import Image
from embed_video.fields import EmbedVideoField



class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status="published")


# Create your models here.
class Post(models.Model):
	objects = models.Manager()      #Our default Manager
	published = PublishedManager()  #Our Custom Model Manager

	STATUS_CHOICES={
     ('draft','Draft'),   
     ('published','Published'), 
    }
	title = models.CharField(max_length=100)
	content = models.TextField()
	author = models.ForeignKey(User,null=True, blank=True, on_delete=models.CASCADE)
	date_posted = models.DateTimeField(default=timezone.now)
	# status =models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
	status =models.CharField(max_length=10,choices=STATUS_CHOICES,default='published')
	image = models.ImageField(null=True, blank=True)
	likes =  models.ManyToManyField(User, related_name='likes', blank=True)
	favourite = models.ManyToManyField(User, related_name='favourite', blank=True)
   
		

  
	def __str__(self):
		return self.title
    
	def total_likes(self):
		return self.likes.count()

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

	def get_absolute_url(self):
			return reverse('post-detail', kwargs={'pk': self.pk})	



	def save(self, *args, **kwargs):
			super(Post, self).save(*args, **kwargs)

			img = Image.open(self.image.path)

			if img.height > 300 or img.width > 300:
				output_size = (300, 300)
				img.thumbnail(output_size)
				img.save(self.image.path)


class Comment(models.Model):
    post = models.ForeignKey(Post,related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User,null=True, blank=True,on_delete=models.CASCADE)	
	# reply = models.ForeignKey('self', null=True, related_name="replies")	
    body = models.TextField(max_length=160)
    date_added = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey('Comment', null=True, related_name="replies", on_delete=models.CASCADE)
  		


def __str__(self):

		return '%s-%s' % (self.post.title, self.name)



class Video(models.Model):
    video = EmbedVideoField()  # same like models.URLField()



class FileAdmin(models.Model):
		fileupload = models.FileField(upload_to='files')  
		title= models.CharField(max_length=50)

		def __str__(self):
			return self.title