from rest_framework.routers import DefaultRouter
from .views import EmitenteViewSet, PagadorViewSet, BoletoViewSet

router = DefaultRouter()

router.register("emitentes", EmitenteViewSet)
router.register("pagadores", PagadorViewSet)
router.register("boletos", BoletoViewSet)

urlpatterns = router.urls