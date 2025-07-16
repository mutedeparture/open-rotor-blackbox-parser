def parse_event_frames(f):
    """
    Parses D (event) frames from the binary log file.
    Captures event ID and optional argument (e.g. arming state).
    """
    data = []
    while True:
        b = f.read(1)
        if not b:
            break
        if b == b'D':
            event = {}
            event_id_byte = f.read(1)
            if not event_id_byte:
                break
            event_id = event_id_byte[0]
            event['event_id'] = event_id
            event['event_name'] = {
                10: 'ARM',
                11: 'FLIGHT_MODE',
                13: 'DISARM',
            }.get(event_id, f'UNKNOWN({event_id})')

            arg = f.read(1)
            if arg:
                event['arg'] = arg[0]

            data.append(event)
    return data