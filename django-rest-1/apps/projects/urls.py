
from rest_framework import routers

from .apis import ProjectsViewSet


router = routers.DefaultRouter()

router.register('api/projects', ProjectsViewSet, 'projects')


urlpatterns = router.urls
