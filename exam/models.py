from django.core.validators import FileExtensionValidator
from django.db import models
from exam_firstt.utils.models import BaseModel
from exam_firstt.users.models import User
from django.contrib.auth import get_user_model


# Create your models here.

"""
class Status(models.TextChoices):
    WATCHED = 'WATCHED', 'Watched'
    NO_WATCHED = 'NO_WATCHED', 'No watched'


class Course(BaseModel):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                              related_name='courses')
    users = models.ManyToManyField(get_user_model(), related_name='courses')



class UserCourse(BaseModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                             related_name='user_courses')
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name='user_courses')
    is_added = models.BooleanField(default=False)


class Lesson(BaseModel):
    courses = models.ForeignKey('Course', on_delete=models.CASCADE,
                                related_name='lessons')
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='videos/',
                             validators=[FileExtensionValidator(['mp4', 'webm'])])
    video_duration = models.IntegerField(default=0)


class UserLesson(BaseModel):

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                             related_name='user_lessons')
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE,
                               related_name='user_lessons')
    status = models.CharField(max_length=15, choices=...)

    watched_time = models.IntegerField(default=0)

    last_seen_date = models.DateField(blank=True, null=True)


class WatchingLesson(BaseModel):
    user_lesson = models.ForeignKey('UserLesson', on_delete=models.CASCADE)
    from_time = models.IntegerField(default=0)
    to_time = models.IntegerField(default=0)

"""


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
        return f"{self.user},{self.video}"
