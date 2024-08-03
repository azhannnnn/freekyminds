from django.urls import path
from .views import *
urlpatterns = [
    path('', home_view, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('restaurants/', restaurant_list_view, name='restaurant_list'),
    path('restaurants/new/', restaurant_create_view, name='restaurant_create'),
    path('restaurants/<int:pk>/edit/', restaurant_update_view, name='restaurant_update'),
    path('restaurants/<int:pk>/delete/', restaurant_delete_view, name='restaurant_delete'),
    path('restaurants/<int:pk>/', restaurant_detail_view, name='restaurant_detail'),
    # Remove or comment out these lines if API views are not needed
    path('api/restaurants/', RestaurantListView.as_view(), name='api_restaurant_list'),
    path('api/restaurants/<int:pk>/', RestaurantDetailView.as_view(), name='api_restaurant_detail'),
    path('api/reviews/', ReviewListView.as_view(), name='api_review_list'),
]
