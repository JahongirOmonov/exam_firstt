from django.db import models
from utils.models import BaseModel
from users.models import User

# Create your models here.


class Video(BaseModel):
    title = models.CharField(max_length=211)
    base_time = models.IntegerField(default=0)
    main_photo = models.ImageField(upload_to='images/', blank=True, null=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name="videos")


    def __str__(self):
        return self.title

class Course(BaseModel):
    title = models.CharField(max_length=211)
    description = models.TextField(blank=True)
    who_buyed = models.ManyToManyField(User, blank=True, related_name="selled_video")
    image = models.ImageField(upload_to="images/")

    price = models.IntegerField(default=0)


    def __str__(self):
        return self.title




class WatchingVideo(BaseModel):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    all_video_time = models.IntegerField()
    already_seen_time = models.IntegerField()


    def __str__(self):
        return f"{self.user},{self.lesson}"





