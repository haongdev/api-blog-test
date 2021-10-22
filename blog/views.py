from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Blog
from .serializers import BlogSerializer


class BlogListAPI(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
