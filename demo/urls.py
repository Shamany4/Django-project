from django.urls import path, include
from . import views
from .views import Second, BookViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('books', BookViewSet)


urlpatterns = [
	path('first', views.first),
	path('second', Second.as_view()),
	path('', include(router.urls))
]
