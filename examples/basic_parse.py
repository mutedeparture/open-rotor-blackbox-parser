import argparse
from blackbox_parser.parser import parse_blackbox_log

def run_example(filepath):
    with open(filepath, "rb") as f:
        result = parse_blackbox_log(f)

    print("\n--- Headers ---")
    print("\n".join(result['headers'][:3]))

    print("\n--- Field Names ---")
    print(result['field_names'])

    print("\n--- First Flight Frame ---")
    print(result['flight_data'][0] if result['flight_data'] else "No flight data")

    print("\n--- First GPS Frame ---")
    print(result['gps_data'][0] if result['gps_data'] else "No GPS data")

    print("\n--- First Event ---")
    print(result['events'][0] if result['events'] else "No events")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Parse a Betaflight Blackbox .bbl file.")
    parser.add_argument("filepath", help="Path to the .bbl file to parse.")
    args = parser.parse_args()

    run_example(args.filepath)