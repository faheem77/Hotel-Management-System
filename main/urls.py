from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
   
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('rooms/', views.RoomListView.as_view(), name='rooms'), 
    path('reservations/', views.ReservationListView.as_view(), name='reservations'),  
    
    path('room/<int:pk>', views.RoomDetailView.as_view(), name='room-detail'), 
    
    path('reservation/<str:pk>', views.ReservationDetailView.as_view(), name='reservation-detail'),
    path('customer/<str:pk>', views.CustomerDetailView.as_view(), name='customer-detail'),  
    path('staff/<str:pk>', views.StaffDetailView.as_view(), name='staff-detail'),  
    path('profile/', login_required(views.ProfileView.as_view()), name='profile'),
    path('guests/', views.GuestListView.as_view(), name='guest-list'),
    path('reserve/', views.reserve, name='reserve'), 
]
