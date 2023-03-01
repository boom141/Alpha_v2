from flask import request, session
from flask_socketio import Namespace, emit, join_room, leave_room

from webApplication.scripts.web_routes.views import active_rooms

class players_lobby(Namespace):
    def on_connect(self):
        print('[CLIENT CONENCTED]:',request.sid)
        join_room(session['room'])

        emit('player_joined', active_rooms, to=session['room'], broadcast=True)
        print(active_rooms)

    def on_disconnect(self):
        print('[CLIENT DISCONENCTED]:',request.sid)

        leave_room(session['room'])
        players = active_rooms[session['room']]['players']
        players.remove(session['name'])

        if len(players) == 0:
            del active_rooms[session['room']]
        

    def on_item_manager(self,data):
        pass