from rest_framework import serializers
from .models import BlogPost

class blogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ["id","title","content","published_date"]
        