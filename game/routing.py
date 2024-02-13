from django.urls import path
from game.consumers.multiplayers.index import MultiPlayer

websocket_urlpatterns = [
    path('wss/multiplayer/', MultiPlayer.as_asgi(), name="wss_multiplayer"),
]

