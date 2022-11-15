from django.db import models
from django.contrib.auth.models import AbstractUser

# User = get_user_model()     ----> this is the built in model. Not recommended

# create your own user model as you might want to customize it on your own
class User(AbstractUser):
    # cellphone_number = models.CharField(max_length=15)
    pass


# Create your models here.
class Lead(models.Model):

    # SOURCE_CHOICES = (
    #     ('YouTube', 'Youtube'),
    #     ('Google', 'Google'),
    #     ('Newsletter', 'Newsletter'),
    # )

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE) #CASCADE means if an agent is deleted the lead associated will be deleted also

    # phoned = models.BooleanField(default=False)
    # source = models.CharField(choices=SOURCE_CHOICES, max_length=100)

    # profile_picture = models.ImageField(blank=True, null=True)
    # special_files = models.FileField(blank=True, null=True) 

   
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # first_name = models.CharField(max_length=20)
    # last_name = models.Model(max_length=20)  --- no need because it is in abstract user, and agent is the one login into the system

    def __str__(self):
        return self.user.email 