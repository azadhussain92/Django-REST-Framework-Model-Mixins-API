from django.db import models

# Create your models here.

SOCIAL_MEDIA = [
    ('FACEBOOK','Facebook'),
    ('INSTAGRAM','Instagram'),
    ('WHATSAPP','Whatsapp'),
    ('SNAPCHAT','Snapchat'),
    ('TWITTER','Twitter'),
    ('TIKTOK','Tiktok'),
]



class userdata(models.Model):
    username = models.CharField(max_length=100)
    age = models.PositiveBigIntegerField()
    phone = models.BigIntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class status(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    social_media = models.CharField(max_length=100,choices=SOCIAL_MEDIA)
    description = models.TextField()
    upload_time = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to="image",null=True,blank=True)
    user = models.ForeignKey(userdata,related_name="userdatas",on_delete=models.CASCADE)

    def __str__(self):
        return self.title