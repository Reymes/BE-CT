from django.urls import path
from .views import (
    AntDocApiView,
    AntDocDetailApiView
)
urlpatterns = [
    path('doc', AntDocApiView.as_view()),
    path('doc/<int:doc_id>', AntDocDetailApiView.as_view()),
]
