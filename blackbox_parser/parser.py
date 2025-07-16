from .reader import parse_headers
from .flight import parse_flight_frames
from .gps import parse_gps_frames
from .events import parse_event_frames

def parse_blackbox_log(f):
    """
    Parses an open .bbl log file object and extracts all telemetry data.

    Returns a dictionary containing headers, field names, flight data, GPS data, and events.
    """
    headers, field_names = parse_headers(f)
    data_start = f.tell()

    flight_data = parse_flight_frames(f, field_names)
    f.seek(data_start)
    gps_data = parse_gps_frames(f)
    f.seek(data_start)
    event_data = parse_event_frames(f)

    return {
        'headers': headers,
        'field_names': field_names,
        'flight_data': flight_data,
        'gps_data': gps_data,
        'events': event_data
    }