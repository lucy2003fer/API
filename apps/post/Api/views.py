from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.post.models import Post
from apps.post.api.serializers import PostSerializers

class PostApiView(ViewSet):
    def list(self, request):
        posts = Post.objects.all()
        serializer = PostSerializers(posts, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def retrieve(self, request, pk=int):
        serializer = PostSerializers(Post.objects.get(pk=pk))
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        

    def create(self, request):
        serializer = PostSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)
