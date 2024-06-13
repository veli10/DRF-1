from rest_framework.generics import ListAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView
from ..models import Blog
from .serializer import BlogSerializers

class BlogListAPIView(ListAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializers
    
class BlogDetailAPIView(RetrieveAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializers
    lookup_field='pk'
    
class BlogDeleteAPIView(DestroyAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializers
    lookup_field='pk'

    
class BlogUpdateAPIView(UpdateAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializers 
    lookup_field='pk'