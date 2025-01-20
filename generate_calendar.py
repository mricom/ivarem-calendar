from calendar_retriever import get_calendar_data_from_api
from icalendar import parse_event
from ical.calendar import Calendar
from ical.calendar_stream import IcsCalendarStream

calendar = Calendar()

data = get_calendar_data_from_api()

for event in data: 
    calendar.events.append(
        parse_event(event)
    )
for event in calendar.timeline:
    print(event.summary)

    

filename = "calendar.ics"
with open(filename, "w") as ics_file:
    ics_file.write(IcsCalendarStream.calendar_to_ics(calendar))
    