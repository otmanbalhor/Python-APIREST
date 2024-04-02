from django.shortcuts import render
from rest_framework import generics
from .models import BlogPost
from .serializers import blogPostSerializer
from rest_framework.views import APIView

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = blogPostSerializer
    
    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
               
class BlogPostRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = blogPostSerializer
    lookup_field = "pk"
    
class BlogPostList(APIView):
    def get(self,request, format=None):
        
        title = request.query_params.get("title","")
        
        if titile:
            
            blog_posts = blogPost.objects.filter(title__icontains=title)
        else:
            
            blog_posts = blogPost.objects.all()
            
        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
