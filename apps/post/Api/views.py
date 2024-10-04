from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.post.models import Post
from apps.post.api.serializers import PostSerializers

class PostModelViewSet(ModelViewSet):
    serializer_class = PostSerializers
    queryset = Post.objects.all()

    '''def list(self, request):
        posts = self.queryset 
        serializer = self.get_serializer(posts, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk=None):
        try:
            post = self.get_object()
            serializer = self.get_serializer(post)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)'''
