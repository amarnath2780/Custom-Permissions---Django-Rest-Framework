from django.urls import include, path
from rest_framework import routers
from data import views
from data.views import CategroryAddViewSet, CategoryViewSet, PostAddViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'posts', PostViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('add-category', CategroryAddViewSet.as_view() , name='add-category'),
    path('add-post', PostAddViewSet.as_view() , name='add-category'),
]