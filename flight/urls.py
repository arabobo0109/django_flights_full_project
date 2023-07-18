from django.urls import path

from flight import views

urlpatterns = [
    path('', views.flights, name='all_flights'),
    path('<int:flight_id>', views.single_flight, name='single_flight'),
    path('text/', views.flights_text, name='all_flights_text'),
    path('buy/<int:flight_id>', views.buy_ticket, name='buy_ticket'),
    path('update_image/<int:flight_id>', views.update_image, name='update_image'),
]
