from django.urls import path, include

# from .views import ItemListCreateView, ItemDetailView
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter()
router.register(r'member', MemberViewSet)
router.register(r'trainer', TrainerViewSet)
router.register(r'paket', PaketViewSet)
router.register(r'transaksi', TransaksiViewSet)


urlpatterns = [
    path('', include(router.urls)),
   
    path('token/',TokenObtainPairView.as_view()),
    path('token/refresh',TokenRefreshView.as_view()),
    path('User-detail/', UserDetailView.as_view(), name='user-detail'),
]