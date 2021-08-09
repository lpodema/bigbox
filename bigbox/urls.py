from django.urls import include, path
from rest_framework import renderers
from bigbox.views import BoxViewSet, ActivityViewSet
from rest_framework.urlpatterns import format_suffix_patterns

box_list = BoxViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

box_detail = BoxViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

activity_list = ActivityViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

activity_detail = ActivityViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = format_suffix_patterns([
    path('', box_list, name='box-list'),
    path('<int:id>/', box_detail, name='box-detail'),
    path('<str:slug>/', box_detail, name='box-by-slug-list'),
    path('<int:id>/activity/', activity_list, name='activity-list'),
    path('<int:id>/activity/<int:pk>/', activity_detail, name='activity-detail'),
])
