from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services.route_service import get_route
from .services.fuel_optimizer import split_route, get_fuel_stops, calculate_total_cost
from django.http import HttpResponse


@api_view(['POST'])
def optimize_route(request):
    start = request.data.get("start")
    end = request.data.get("end")

    route = get_route(start, end)

    if "error" in route:
        return Response({
            "error": route["error"]
        })

    distance = route['distance']

    stops = split_route(distance)
    fuel_stops = get_fuel_stops(stops)

    avg_price = sum([s['price'] for s in fuel_stops]) / len(fuel_stops)
    total_cost = calculate_total_cost(distance, avg_price)

    return Response({
        "distance": distance,
        "fuel_stops": fuel_stops,
        "total_cost": total_cost,
        "route": route['geometry']
    })


def home(request):
    return HttpResponse("""
        <center>
            <h1>Fuel Optimization API is Running</h1>
            
            <p><b>Endpoint:</b></p>
            <a href="/api/optimize-route/">/api/optimize-route/</a>

            <p><b>How to use:</b></p>
            <p>1. Open the endpoint above</p>
            <p>2. Scroll down to the content box</p>
            <p>3. Paste this JSON:</p>

            <pre>
{
  "start": [-74.0060, 40.7128],
  "end": [-118.2437, 34.0522]
}
            </pre>

            <p>4. Click POST to get optimized fuel stops and total cost</p>
        </center>
    """)