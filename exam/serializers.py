from .models import Video, Course
from rest_framework import serializers

class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = (
            "title",
            "base_time",
            "main_photo",
            "course"
        )



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            "title",
            "description",
            "image",
            "price",
        )

