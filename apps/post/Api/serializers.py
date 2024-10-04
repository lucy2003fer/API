from rest_framework.serializers import ModelSerializer
from apps.post.models import Post

class PostSerializers(ModelSerializer):  # Corrige aquí
    class Meta:
        model = Post
        fields = '__all__'
