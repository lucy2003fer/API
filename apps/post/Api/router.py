from rest_framework.routers import DefaultRouter
from apps.post.api.views import PostModelViewSet

router_post = DefaultRouter()
router_post.register(prefix="posts", basename="post", viewset=PostModelViewSet)
