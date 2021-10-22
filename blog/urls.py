from django.urls import path
from .views import BlogListAPI
urlpatterns = [
    path('', BlogListAPI.as_view(), name='blog_list')
]
