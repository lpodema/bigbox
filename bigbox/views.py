from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, decorators
from bigbox.models import Box, Activity
from bigbox.serializers import BoxSerializer, ActivitySerializer
from django.db.models import Prefetch
from django.core.exceptions import ObjectDoesNotExist


class MultipleFieldLookupMixin:
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """

    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            try:                                  # Get the result with one or more fields.
                filter[field] = self.kwargs[field]
            except Exception:
                pass
        return get_object_or_404(queryset, **filter)  # Lookup the object


class BoxViewSet(MultipleFieldLookupMixin, viewsets.ModelViewSet):
    model = Box
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
    lookup_fields = ['id', 'slug']

class ActivityViewSet(viewsets.ModelViewSet):
    model = Activity

    def get_queryset(self):
        if 'id' in self.kwargs:
            try:
                qs = Box.objects.get(pk=self.kwargs["id"]).activities.all()
            except ObjectDoesNotExist:
                pass
            if 'activity_id' in self.kwargs:
                try:
                    print(self.kwargs["id"], self.kwargs['activity_id'])
                    qs = qs.get(id=self.kwargs["activity_id"])
                    print(qs)
                    return qs
                except ObjectDoesNotExist:
                    pass
            else:
                return qs
        else:
            return Activity.objects.all()
    
    #queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    lookup_field = 'activity_id'
