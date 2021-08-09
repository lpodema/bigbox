from django.http.response import Http404
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from bigbox.models import Box, Activity
from bigbox.serializers import BoxSerializer, ActivitySerializer
from django.core.exceptions import ObjectDoesNotExist


class MultipleFieldLookupMixin:
    """
    Codigo tomado de la documentacion de django-rest-framework
    """

    def get_object(self):
        # Get the base queryset
        queryset = self.get_queryset()
        # Apply any filter backends
        queryset = self.filter_queryset(queryset)
        filter = {}
        for field in self.lookup_fields:
            # Get the result with one or more fields.
            try:
                filter[field] = self.kwargs[field]
            except Exception:
                pass
        return get_object_or_404(queryset, **filter)    # Lookup the object


class BoxViewSet(MultipleFieldLookupMixin, viewsets.ModelViewSet):
    model = Box
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
    lookup_fields = ['id', 'slug']


class ActivityViewSet(MultipleFieldLookupMixin, viewsets.ModelViewSet):
    model = Activity

    def get_queryset(self):
        if 'id' in self.kwargs:
            try:
                qs = Box.objects.get(pk=self.kwargs["id"]).activities.all()
            except ObjectDoesNotExist:
                raise Http404
            if 'activity_id' in self.kwargs:
                try:
                    return qs.filter(id=self.kwargs["activity_id"])
                except ObjectDoesNotExist:
                    raise Http404
            else:
                return qs
        else:
            return Activity.objects.all()

    serializer_class = ActivitySerializer
    lookup_fields = ['pk']
