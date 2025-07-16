# blackbox_parser/cli.py
import argparse
from .parser import parse_blackbox_log

def main():
    parser = argparse.ArgumentParser(description="Parse a Blackbox .bbl file")
    parser.add_argument("filepath", help="Path to the .bbl log file")
    args = parser.parse_args()

    with open(args.filepath, "rb") as f:
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
