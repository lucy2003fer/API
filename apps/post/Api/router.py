from rest_framework.routers import DefaultRouter
from apps.post.api.views import PostApiView  # Asegúrate de que el nombre de la clase es correcto

router_post = DefaultRouter()
router_post.register(prefix="posts", basename="post", viewset=PostApiView)
