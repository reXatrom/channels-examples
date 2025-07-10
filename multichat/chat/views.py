from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room


@login_required
# def index(request):
#     """
#     Root page view. This is essentially a single-page app, if you ignore the
#     login and admin parts.
#     """
#     # Get a list of rooms, ordered alphabetically
#     rooms = Room.objects.order_by("title")

#     # Render that in the index template
#     return render(request, "index.html", {
#         "rooms": rooms,
#     })

def room(request, room_name):
    return render(request, "room.html", {"room_name": room_name})

def lobby(request):
    rooms = Room.objects.all()
    return render(request, 'lobby.html', {'rooms': rooms})