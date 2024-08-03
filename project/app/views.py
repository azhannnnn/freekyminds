from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Restaurant, Review
from .forms import RestaurantForm, ReviewForm
from django.http import JsonResponse

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def home_view(request):
    return render(request, 'home.html')

def restaurant_list_view(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant_list.html', {'restaurants': restaurants})

def restaurant_create_view(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant_list')
    else:
        form = RestaurantForm()
    return render(request, 'restaurant_form.html', {'form': form})

def restaurant_update_view(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('restaurant_list')
    else:
        form = RestaurantForm(instance=restaurant)
    return render(request, 'restaurant_form.html', {'form': form})

def restaurant_delete_view(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        restaurant.delete()
        return redirect('restaurant_list')
    return render(request, 'restaurant_confirm_delete.html', {'restaurant': restaurant})

def restaurant_detail_view(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    reviews = Review.objects.filter(restaurant=restaurant)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.restaurant = restaurant
            review.save()
            return redirect('restaurant_detail', pk=restaurant.pk)
    else:
        form = ReviewForm()
    return render(request, 'restaurant_detail.html', {'restaurant': restaurant, 'reviews': reviews, 'form': form})


from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RestaurantSerializer, ReviewSerializer

class RestaurantListView(APIView):
    def get(self, request):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

class RestaurantDetailView(APIView):
    def get(self, request, pk):
        restaurant = get_object_or_404(Restaurant, pk=pk)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)

class ReviewListView(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)