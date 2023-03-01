import random
from flask import Blueprint, render_template, redirect, url_for, request, session
from string import ascii_uppercase

views = Blueprint('views', __name__)

active_rooms = {}

def generate_unique_code(length):
    while 1:
        code_generated = ''
        for _ in range(length):
            code_generated += random.choice(ascii_uppercase)

        if code_generated not in active_rooms:
            break
        

    return code_generated

@views.route('/', methods=['GET', 'POST'])
def home():
    session.clear()
    if request.method == 'POST':
        player_name = request.form.get('player-name')
        room_name = request.form.get('room-name')
        new_session = request.form.get('new-session', False)
        join_session = request.form.get('join-session', False)

        if new_session != False:
            room_code = generate_unique_code(5)
            active_rooms[room_name] = {'host': player_name, 'room_code':room_code, 'players': [player_name]}
            session['name'] = player_name
            session['room'] = room_name

            return redirect(url_for('.players_lobby'))
        

    else:
        return render_template('index.html')


@views.route('/lobby', methods=['GET', 'POST'])
def players_lobby():
    if 'room' in session:
        return render_template('lobby.html', room_name = session['room'])
    else:
        return redirect(url_for('.home'))