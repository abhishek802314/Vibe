from rest_framework import serializers
from .models import Restaurant, RestaurantReview, Event, EventReview

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

    
class RestaurantReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantReview
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
    
class EventReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventReview
        fields = '__all__'