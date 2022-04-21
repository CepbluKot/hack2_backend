from rest_framework import routers

from . import api

router = routers.DefaultRouter()
router.register('', api.CustomUserModelViewSet)
from django.urls import include, path
from . import routers, views

urlpatterns = [
    path('data/', views.UserRetrieveUpdateDestroyAPIView.as_view(),
         name='user-data'),
    path('users/', include(routers.router.urls)),
    path('users/<int:pk>/', api.CustomUserModelViewSet.as_view({'get': 'retrieve'}), name='user-detail'),
    path('sellers/', api.SellerViewSet.as_view({'get': 'list', 'post': 'create'}), name='sellers'),
    path('qs/create/', api.QuotationSessionViewSet.as_view({'post': 'create'}), name='QS'),
    path('qs/all/', api.QuotationSessionAllViewSet.as_view({'get': 'list'}), name='QSall'),
    path('qs/<int:pk>/', api.QuotationSessionAllViewSet.as_view({'get': 'retrieve'}), name='QSall'),
    path('qs-history/insert/', api.QSPriceHistoryViewSet.as_view({'post': 'create'}), name='QSPostHistory'),
    path('qs-history/all/', api.QSPriceHistoryViewSet.as_view({'get': 'list'}), name='QSGetHistory'),
    path('qs-history/<int:pk>/', api.QSPriceHistoryViewSet.as_view({'get': 'retrieve'}), name='QSGetHistory'),
    path('user-sessions/update/', api.UserStatusViewSet.as_view({'get': 'list', 'post': 'create'}), name='UserStatus'),
    path('user-sessions/all/', api.UserStatusViewSet.as_view({'get': 'list'}), name='UserStatus'),
    path('user-sessions/<int:pk>/', api.UserStatusViewSet.as_view({'get': 'retrieve'}), name='UserStatus'),
    ]
