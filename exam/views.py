from django.shortcuts import render
from .serializers import LessonSerializer
from rest_framework import generics
from .models import Lesson
#
# # Create your views here.
#
# class LessonListApiView(generics.ListAPIView):
#     queryset = Video.objects.all()
#     serializer_class = VideosSerializer
#
#
# class CourseListApiView(generics.ListAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer



class LessonListApiView(generics.ListAPIView):
    queryset = Lesson.objects.all().prefetch_related(
        "user_lessons", "course__user_courses"
    ).select_related("course")

    serializer_class = LessonSerializer

    def get_queryset(self):
        user = self.request.user
        lessons = super().get_queryset().filter(
            course__user_courses__user=user,
            # user_lessons__user=user,
        )


        return lessons
