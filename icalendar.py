from datetime import date
import uuid

from ical.calendar import Calendar
from ical.event import Event

def parse_event(event: dict): 
    # start_date = event["ophaaldatum"].replace(hour=19, minute=0)
    start_date = event["ophaaldatum"]
    end_date = event["ophaaldatum"]
    # end_date = event["ophaaldatum"].replace(hour=23, minute=59)
    
    return Event(
        summary=event["fractie"], 
        dtstart=start_date, 
        dtend=end_date,
        categories=[event["fractieCode"]], 
    )
    

 
    