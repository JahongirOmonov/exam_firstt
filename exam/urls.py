from django.urls import path
from .views import LessonListApiView


urlpatterns = [
    path('', LessonListApiView.as_view()),

]
