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
    # Your logic to fetch data or perform other operations
    all_flights = Flight.objects.all()
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



