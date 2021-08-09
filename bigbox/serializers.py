from bigbox.models import Box, Activity
import urllib
from rest_framework import serializers
from rest_framework.reverse import reverse


class CustomHyperlinkedIdentityField(serializers.HyperlinkedIdentityField):
    def get_url(self, obj, view_name, request, format):
        from rest_framework.reverse import reverse
        lookup_field_id = self.lookup_field + '_id'
        lookup_field_value = getattr(obj, lookup_field_id, None)
        result = '{}?{}'.format(
            reverse(view_name, kwargs={}, request=request, format=format),
            urllib.urlencode({self.lookup_field: lookup_field_value})
        )
        return result


class ActivitySerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    def get_url(self, obj):
        request = self.context['request']
        print(obj)
        return reverse('bigbox:activity-detail', kwargs={'id': obj.box_set.first().pk, 'activity_id': obj.pk}, request=request)

    class Meta:
        model = Activity
        fields = ['pk', 'url', 'name', 'internal_name', 'description',
                  'category', 'reasons', 'purchase_available']


class ActivityNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['name', 'description']


class BoxSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    category = serializers.StringRelatedField()
    activities = serializers.SerializerMethodField()
    activity = serializers.SerializerMethodField()
    # def get_activity(self, obj):
    #    activities = obj.activities.all()
    #    return ActivitySerializer(activities, many=True).data

    def get_activity(self, obj):
        request = self.context['request']
        return reverse('bigbox:activity-list', kwargs={'id':obj.id}, request=request)

    def get_url(self, obj):
        request = self.context['request']
        return reverse('bigbox:box-detail', kwargs={'id': obj.id}, request=request)

    def get_activities(self, obj):
        activities = obj.activities.all()[:5]
        return ActivityNameSerializer(activities, many=True).data

    class Meta:
        model = Box
        lookup_field = 'slug'
        fields = ['url', 'slug', 'name', 'internal_name', 'description', 'activity',
                  'category', 'activities', 'price', 'purchase_available']
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
