from django.urls import path
from .views import VideoListApiView, CourseListApiView


urlpatterns = [
    path('videos/', VideoListApiView.as_view()),
    path('courses/', CourseListApiView.as_view())
]