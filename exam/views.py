from django.shortcuts import render
from .serializers import VideosSerializer, CourseSerializer
from rest_framework import generics
from .models import Video, Course

# Create your views here.

class VideoListApiView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideosSerializer


class CourseListApiView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



  """
  Thank for everything
  """
