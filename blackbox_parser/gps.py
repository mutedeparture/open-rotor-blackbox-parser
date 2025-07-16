from .decoder import read_signed_varint

def parse_gps_frames(f):
    """
    Parses G (GPS) frames from the binary log file.
    Each frame includes time, number of satellites, coordinates, altitude, speed, and ground course.
    """
    data = []
    while True:
        b = f.read(1)
        if not b:
            break
        if b == b'G':
            fields = [read_signed_varint(f) for _ in range(7)]
            if None not in fields:
                entry = {
                    'time': fields[0],
                    'sats': fields[1],
                    'lat': fields[2] / 1e7,
                    'lon': fields[3] / 1e7,
                    'alt': fields[4] / 100,
                    'speed': fields[5] / 100,
                    'course': fields[6] / 10,
                }
                data.append(entry)
    return data
