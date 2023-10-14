from rest_framework.routers import DefaultRouter
from .views import PasswordGenerateViewSet

router = DefaultRouter()
router.register(r"passwords", PasswordGenerateViewSet, basename="password")

urlpatterns = router.urls
