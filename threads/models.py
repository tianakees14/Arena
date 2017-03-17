from django.db import models

# Create your models here.
class Profile(models.Model):
	user_name = models.CharField(((u"User Name")),max_length = 100)
	name = models.CharField(((u"Name")),max_length = 100)
	email_id = models.EmailField()
	image =  models.ImageField(upload_to = 'img/', default = 'img/user.jpg')
	score = models.IntegerField()

	def __str__(self):
		return self.user_name+self.name+self.email_id+str(self.score)

	class Meta:
		verbose_name = "Profile"
		verbose_name_plural = "Profile"		


class Questions(models.Model):
	question = models.CharField((u"Question"),max_length = 100)		
	user_name = models.CharField((u"User Name"),max_length = 100)	
	posted = models.DateTimeField(auto_now_add=True)
	domain = models.CharField((u"Domain"),max_length = 100)	

	def __str__(self):
		return self.user_name+str(self.posted)+self.question+str(id)

	class Meta:
		verbose_name = "Questions"
		verbose_name_plural = "Questions"


class Replies(models.Model):
	question_id = models.IntegerField()
	posted = models.DateTimeField(auto_now_add=True)
	rank = models.IntegerField()
	reply = models.CharField((u"Reply"),max_length = 100)
	votes = models.IntegerField()
	domain = models.CharField((u"Domain"),max_length = 100)	


	def __str__(self):
		return str(self.question_id)+str(votes)+str(posted)+str(rank)+reply+str(id)

	class Meta:
		verbose_name = "Replies"
		verbose_name_plural = "Replies"

class ThreadReplies(models.Model):
	reply_id = models.IntegerField()	
	reply = models.CharField((u"Reply"),max_length = 100)
	votes = models.IntegerField()
	rank = models.IntegerField()
	posted = models.DateTimeField(auto_now_add=True)
	



	def __str__(self):
		return str(self.reply_id)+str(votes)+str(posted)+str(rank)+reply+str(id)

	class Meta:
		verbose_name = "Thread Replies"
		verbose_name_plural = "Thread Replies"


class Requests(models.Model):
	user_name = models.CharField(((u"User Name")),max_length = 100)
	requestor = models.CharField(((u"User Name")),max_length = 100)

	def __str__(self):
		self.user_name+self.requestor

class Followers(models.Model):
	user_name = models.CharField(((u"User Name")),max_length = 100)
	follower = models.CharField(((u"User Name")),max_length = 100)


	def __str__(self):
		self.user_name+self.follower