from app.models.events import Event


event1 = Event("03/04/2021", "duck's big birthday", 20, "room1", "big birthday bash", True)
event2 = Event("30/05/2021", "bill and ben wedding", 150, "big ballroom", "wedding of the year", True)

events = [event1, event2]

def add_new_event(event):
    events.append(event)




