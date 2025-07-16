def parse_headers(f):
    """
    Parses header lines (starting with 'H' or '#') from the file.
    Extracts metadata and field names for I/P frames.
    """
    headers = []
    field_names = []
    while True:
        pos = f.tell()
        line = f.readline()
        if not line:
            break
        if line.startswith((b'H', b'#')):
            try:
                decoded = line.decode('utf-8').strip()
            except UnicodeDecodeError:
                f.seek(pos)
                break
            headers.append(decoded)
            if decoded.startswith("H Field I name:"):
                field_names = [s.strip() for s in decoded.split(":", 1)[1].split(",")]
        else:
            f.seek(pos)
            break
    return headers, field_names