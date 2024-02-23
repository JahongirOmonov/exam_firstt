from django.core.validators import FileExtensionValidator
from django.db import models
from utils.models import BaseModel
from users.models import User
from django.contrib.auth import get_user_model


class Course(BaseModel):
    title = models.CharField(max_length=211)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/")
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class UserCourse(BaseModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name='user_courses')

    def __str__(self):
        return f"{self.user} -- > {self.course}"


class Lesson(BaseModel):
    title = models.CharField(max_length=211)
    video = models.FileField(upload_to='videos/')
    course = models.ForeignKey('Course', on_delete=models.CASCADE,
                               related_name="lessons")
    duration = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class UserLesson(BaseModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE,
                               related_name='user_lessons')
    status = models.BooleanField(default=False)
    watched_time = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user} -- > {self.lesson}"




class WatchingLesson(BaseModel):
    user_lesson = models.ForeignKey('UserLesson', on_delete=models.CASCADE)
    from_time = models.IntegerField(default=0)
    to_time = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user_lesson}"



