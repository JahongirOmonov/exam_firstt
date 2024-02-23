from .models import Lesson, Course, UserCourse, UserLesson, WatchingLesson
from rest_framework import serializers


class UserLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLesson
        fields = (
            'status',
            'watched_time'
        )


class LessonSerializer(serializers.ModelSerializer):

    user_lessons = UserLessonSerializer()

    class Meta:
        model = Lesson
        fields = (
            "title",
            "video",
            "duration",
            "user_lessons",
        )


# class CourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Course
#         fields = (
#             "title",
#             "description",
#             "image",
#             "price",
#         )



