from django.db import models
from django.contrib.auth.models import User
from django.core.files import File

# Create your models here.


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    photo = models.ImageField(upload_to="userPics")

    def __str__(self):
        return self.user.username


class Bunk(models.Model):
    from_user = models.ForeignKey(UserProfile,
        related_name='from_user')

    to_user = models.ForeignKey(UserProfile,
        related_name='to_user')
    
    time = models.DateTimeField('date bunked')

    def __str__(self):
        return "<Bunk: from(%s) to (%s)>"%(self.from_user, self.to_user)




def addUser(username, pic_file_name):
    theUser = User.objects.create_user(username=username)
#    prof.user = theUser
    f = File(open(pic_file_name),'r')
 #   prof.photo = f
    prof = UserProfile(user=theUser,photo=f)
    prof.save()
