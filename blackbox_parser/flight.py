from .decoder import read_signed_varint

def parse_flight_frames(f, field_names):
    """
    Parses I and P frames (flight data) from the binary log file.
    Uses delta or absolute encoding depending on frame type.
    """
    current_values = [0] * len(field_names)
    data = []

    while True:
        b = f.read(1)
        if not b:
            break

        if b == b'I' or b == b'P':
            is_absolute = b == b'I'
            temp_values = current_values[:]
            frame_ok = True

            for i in range(len(field_names)):
                delta = read_signed_varint(f)
                if delta is None:
                    frame_ok = False
                    break
                if is_absolute:
                    temp_values[i] = delta
                else:
                    temp_values[i] += delta

            if frame_ok:
                current_values = temp_values
                entry = dict(zip(field_names, current_values))
                entry['frame_type'] = b.decode()
                data.append(entry)

    return data