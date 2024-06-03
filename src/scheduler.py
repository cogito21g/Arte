import datetime

schedule = {}

def add_event(date, event):
    if date in schedule:
        schedule[date].append(event)
    else:
        schedule[date] = [event]

def get_events(date):
    return schedule.get(date, [])