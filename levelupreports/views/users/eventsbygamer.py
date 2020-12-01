"""Module for generating events by gamer report"""
import sqlite3
from django.shortcuts import render
from levelupapi.models import Event
from levelupreports.views import Connection

def gamerevent_list(request):
    """Function to build an HTML report of events by gamer"""
    if request.method == 'GET':
        # Connect to project database
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            # Query for all events by user
            db_cursor.execute("""
                SELECT
                    e.organizer_id,
                    u.first_name || ' ' || u.last_name AS full_name,
                    e.id,
                    e.date,
                    e.time,
                    g.title
                FROM
                    levelupapi_event e
                JOIN
                    levelupapi_game g ON e.game_id = g.id
                JOIN
                    auth_user u ON e.organizer_id = u.id
            """)

            dataset = db_cursor.fetchall()

            events_by_user = {}
            
            for row in dataset:
                # create an Event instance and set its properties
                event = Event()
                event.id = row["id"]
                event.date = row["date"]
                event.time = row["time"]
                event.game_name = row["title"]

                uid = row["organizer_id"]

                if uid in events_by_user:
                    events_by_user[uid]['events'].append(event)

                else:
                    events_by_user[uid] = {}
                    events_by_user[uid]["organizer_id"] = uid
                    events_by_user[uid]["full_name"] = row["full_name"]
                    events_by_user[uid]["events"] = [event]

        list_of_users_with_events = events_by_user.values()

        template = 'users/list_with_events.html'
        context = {
            'eventuser_list': list_of_users_with_events
        }

        return render(request, template, context)
