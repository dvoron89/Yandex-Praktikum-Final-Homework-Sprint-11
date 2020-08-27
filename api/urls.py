from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (CategoryViewSet,
                    CommentViewSet,
                    GenreViewSet,
                    ReviewViewSet,
                    TitleViewSet,
                    UserViewSet,
                    get_confirmation_code,
                    get_jwt_token)


router = DefaultRouter()

router.register('users', UserViewSet)
router.register('categories', CategoryViewSet)
router.register('genres', GenreViewSet)
router.register('titles', TitleViewSet)
router.register(r'titles/(?P<title>\d+)/reviews',
                ReviewViewSet, basename='reviews')
router.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
                CommentViewSet, basename='comment')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/email/', get_confirmation_code),
    path('v1/auth/token/', get_jwt_token),
]
