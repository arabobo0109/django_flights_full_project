from django.urls import path

from flight import views

urlpatterns = [
    path('', views.flights, name='all_flights'),
    path('text/', views.flights_text, name='all_flights_text'),
    path('buy/<int:flight_id>', views.buy_ticket, name='buy_ticket'),
]
