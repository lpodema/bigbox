from bigbox.models import Box, Activity
from rest_framework import serializers
from rest_framework.reverse import reverse


class ActivitySerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        request = self.context['request']
        box_id = request.resolver_match.kwargs.get('id', None)
        return reverse('bigbox:activity-detail', kwargs={'id': box_id, 'activity_id': obj.pk}, request=request)

    reasons = serializers.StringRelatedField(many=True)
    category = serializers.StringRelatedField()

    class Meta:
        model = Activity
        fields = ['url', 'name', 'internal_name', 'description',
                  'category', 'reasons', 'purchase_available']


class ActivityNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['name']


class BoxSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    category = serializers.StringRelatedField()
    activities = serializers.SerializerMethodField()
    activity = serializers.SerializerMethodField()

    def get_activity(self, obj):
        request = self.context['request']
        return reverse('bigbox:activity-list', kwargs={'id': obj.id}, request=request)

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
