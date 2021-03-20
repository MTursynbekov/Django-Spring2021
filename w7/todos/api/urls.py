from rest_framework.routers import DefaultRouter
from .views import TODOListViewSet

router = DefaultRouter()
router.register(r'todos', TODOListViewSet, basename='api')

urlpatterns = router.urls
