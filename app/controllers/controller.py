from app import app
from flask import render_template, request
from app.models.events import Event
from app.models.event_details import events, add_new_event


@app.route('/')
def index():
        return render_template('index.html', title="Bookings", events=events)


@app.route('/', methods=['POST'])
def add_event():
    event_date = request.form['date']
    event_name = request.form['name']
    event_guests = request.form['guests']
    event_room = request.form['room']
    event_description = request.form['description']
    event_recurring = request.form['recurring']
    new_event = Event(event_date, event_name, event_guests, event_room, event_description, event_recurring)
    add_new_event(new_event)
    return render_template('index.html', title="Bookings", events=events)
  
