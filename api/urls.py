from posixpath import basename
from rest_framework_simplejwt.views import (

    TokenRefreshView,
)
from xml.etree.ElementInclude import include
from django.urls import path, include


from .views import userView, cardView, getRoutes, MyTokenObtainPairView, userToPremium, shortV2Set, shortV2View, PostView, PostSet, GetPostView, CommentView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('shortsetV2', shortV2Set, basename="shortV2Set")
router.register('postset', PostSet, basename="postset")

urlpatterns = [
    path('users/', userView.as_view(), name='users_list'),
    path('users/<int:id>', userView.as_view(), name='users_process'),
    path('cards/', cardView.as_view(), name='cards_list'),
    path('cards/<str:section>', cardView.as_view(), name='cards_list3'),
    path('usercards/<int:id>', cardView.as_view(), name='cards_list2'),
    path('delcard/<int:card>', cardView.as_view(), name='cards_list2'),
    # path('shorts/', shortView.as_view(), name='shorts_list'),
    path('shortsV2/', shortV2View.as_view(), name='shorts_list'),

    path('routes/', getRoutes),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('makepremium/<int:id>', userToPremium.as_view(), name='user_to_premium'),
    path('post/<int:id>', GetPostView.as_view(), name='post'),
    path('posts/', PostView.as_view(), name='posts list'),
    path('posts/<int:id>', PostView.as_view(), name="liked posts by user"),
    path('comments/', CommentView.as_view(), name="post comment"),
    path('comments/<int:id>', CommentView.as_view(), name="liked posts by user"),
    path('', include(router.urls)),
]
