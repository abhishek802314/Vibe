from django.shortcuts import render, get_object_or_404
from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Restaurant, RestaurantReview, Event, EventReview
from .serializers import RestaurantSerializer, RestaurantReviewSerializer, EventSerializer, EventReviewSerializer

class RestaurantList(generics.GenericAPIView):
    serializer_class = RestaurantSerializer

    def get(self, request, format=None):
        restaurants = Restaurant.objects.all()
        serializer = self.get_serializer(restaurants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class RestaurantDetail(generics.GenericAPIView):
    serializer_class = RestaurantSerializer

    def get_object(self, restaurant_id):
        try:
            return Restaurant.objects.get(pk=restaurant_id)
        except Restaurant.DoesNotExist:
            raise Http404
        
    def get(self, request, restaurant_id):
        restaurant = self.get_object(restaurant_id)
        serializer = self.get_serializer(restaurant)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, restaurant_id):
        restaurant = self.get_object(restaurant_id)
        serializer = self.get_serializer(restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, restaurant_id):
        restaurant = self.get_object(restaurant_id)
        restaurant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class RestaurantReviewList(generics.GenericAPIView):
    serializer_class = RestaurantReviewSerializer

    def get(self, request):
        reviews = RestaurantReview.objects.all()
        serializer = self.get_serializer(reviews, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RestaurantReviewDetail(generics.GenericAPIView):
    serializer_class = RestaurantReviewSerializer

    def get_object(self, review_id):
        try:
            return RestaurantReview.objects.get(pk=review_id)
        except RestaurantReview.DoesNotExist:
            raise Http404
        
    def get(self, request, review_id):
        review = self.get_object(review_id)
        serializer = self.get_serializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, review_id):
        review = self.get_object(review_id)
        serializer = self.get_serializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, review_id):
        review = self.get_object(review_id)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class GetRestaurantReviews(generics.GenericAPIView):
    serializer_class = RestaurantReviewSerializer

    def get(self, request, restaurant_id):
        reviews = RestaurantReview.objects.filter(restaurant_id=restaurant_id)
        serializer = self.get_serializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Event views
class EventList(generics.GenericAPIView):
    serializer_class = EventSerializer

    def get(self, request):
        events = Event.objects.all()
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EventDetail(generics.GenericAPIView):
    serializer_class = EventSerializer

    def get_object(self, event_id):
        try:
            return Event.objects.get(pk=event_id)
        except Event.DoesNotExist:
            raise Http404
        
    def get(self, request, event_id):
        event = self.get_object(event_id)
        serializer = self.get_serializer(event)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, event_id):
        event = self.get_object(event_id)
        serializer = self.get_serializer(event, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, event_id):
        event = self.get_object(event_id)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# Event Review Views

class EventReviewList(generics.GenericAPIView):
    serializer_class = EventReviewSerializer

    def get(self, request):
        reviews = EventReview.objects.all()
        serializer = self.get_serializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class EventReviewDetail(generics.GenericAPIView):
    serializer_class = EventReviewSerializer

    def get_object(self, review_id):
        try:
            return EventReview.objects.all()
        except EventReview.DoesNotExist:
            raise Http404
        
    def get(self, request, review_id):
        review = self.get_object(review_id)
        serializer = self.get_serializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, review_id):
        review = self.get_object(review_id)
        serializer = self.get_serializer(review, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, review_id):
        review = self.get_object(review_id)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# Get Event reviews

class GetEventReviews(generics.GenericAPIView):
    serializer_class = EventReviewSerializer
    
    def get(self, request, event_id):
        reviews = EventReview.objects.filter(event_id=event_id)
        serializer = self.get_serializer(reviews)
        return Response(serializer.data, status=status.HTTP_200_OK)
           
        

# Get all saved resturants and events for a user

class GetRestaurantByUser(generics.GenericAPIView):
    serializer_class = RestaurantSerializer

    def get(self, request, username):
        restaurants = Restaurant.objects.filter(username=username)
        serializer = self.get_serializer(restaurants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class GetEventsByUser(generics.GenericAPIView):
    serializer_class = EventSerializer

    def get(self, request, username):
        events = Event.objects.filter(username=username)
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
# Get Top Reviewed Restaurants

class GetTopReviewed(generics.GenericAPIView):
    serializer_class1 = RestaurantReview
    serializer_class2 = EventReview

    def get_restaurants(self):
        return RestaurantReview.objects.order_by('-rating')

    def get_events(self):
        return EventReview.objects.order_by('-rating')

    def get(self, request):
        top_restaurants = self.get_restaurants()
        restaurant_serializer = self.get_serializer1(top_restaurants, many=True)
        top_events = self.get_events()
        event_serializer = self.get_serializer2(top_events, many=True)

        return Response({
            'restaurants': restaurant_serializer.data,
            'events': event_serializer.data
        })

    
# Get latest reviews of restaurants and events

class GetLatestResults(generics.GenericAPIView):
    restaurant_serializer = RestaurantSerializer
    event_serializer = EventSerializer
    restaurant_review_serializer = RestaurantReviewSerializer
    event_review_serializer = EventReviewSerializer

    def get(self, request):
        response_dict = {}

        restaurants = Restaurant.objects.all()
        for idx, item in enumerate(restaurants):
            reviews = RestaurantReview.objects.filter(restaurant_id = item.id)
            if reviews.exists():
                restaurant_data = self.restaurant_serializer(item).data
                reviews_data = self.restaurant_review_serializer(reviews, many=True).data
                response_dict.update({f"restaurant_entry{idx}": {
                    "restaurant": restaurant_data,
                    "reviews": reviews_data
                }})

        events = Event.objects.all()
        for idx, item in enumerate(events):
            reviews = EventReview.objects.filter(event_id = item.id)
            if reviews.exists():
                event_data = self.event_serializer(item).data
                reviews_data = self.event_review_serializer(reviews, many=True).data
                response_dict.update({f"event_entry{idx}": {
                    "restaurant": event_data,
                    "reviews": reviews_data
                }})

        return Response(response_dict)

# Get Restaurant by name 

class GetRestaurantByName(generics.GenericAPIView):
    serializer_class = RestaurantSerializer

    def get(self, request, name, username):
        queryset = Restaurant.objects.filter(name=name, username=username)
        restaurant = get_object_or_404(queryset)
        serilizer = self.get_serializer(restaurant)
        return Response(serilizer.data)
    

# get Events by name

class GetEventByName(generics.GenericAPIView):
    serializer_class = EventSerializer

    def get(self, request, name, username):
        queryset = Event.objects.filter(name=name, username=username)
        event = get_object_or_404(queryset)
        serializer = self.get_serializer(event)
        return Response(serializer.data)