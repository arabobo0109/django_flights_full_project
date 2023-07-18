from django.http import HttpResponse
from django.shortcuts import render,redirect

from flight.models import Flight

def buy_ticket(request, flight_id):
    if request.method == 'POST':
        number = request.POST.get('number')
        print("NUMBER IS", number)
    flight = Flight.objects.get(id=flight_id)
    flight.tickets = flight.tickets - int(number)
    flight.save()
    return redirect('all_flights')
    

def flights(request):
    # filter by tickets number - get tickets number from GET request
    tickets_max = request.GET.get('tickets_max')
    all_flights = Flight.objects.all()
    if tickets_max:
        all_flights = all_flights.filter(tickets__lt=tickets_max)
    context = {
        'flights': all_flights  # Replace 'data' with the data you want to pass to the template
    }
    return render(request, 'flights.html', context)

def flights_text(request):
    all_flights = Flight.objects.all()
    mystr = ""
    for flight in all_flights:
        mystr += str(flight)
        mystr += "<br>"
    return HttpResponse(f"This is a list of flights!<br>{mystr}")



