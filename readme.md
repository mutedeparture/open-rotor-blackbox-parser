# Open Rotor Blackbox Parser

A lightweight Python parser for Betaflight Blackbox `.bbl` logs. Extracts complete telemetry including flight data, GPS, and events — all without CSV exports or third-party GUIs.

---

## 🚀 Features

- Parse raw `.bbl` files directly
- Extract:
  - Flight data (stick commands, motors, sensors)
  - GPS frames (lat/lon, alt, speed, heading)
  - Events (arming/disarming, failsafe, flight mode changes)
- Modular Python codebase for easy extension
- Example scripts for testing and development

---

## 🛠️ Usage

### CLI

```bash
python -m examples.basic_parse path/to/log.bbl
```

# API
```python
from blackbox_parser.parser import parse_blackbox_log

with open("flight_log.bbl", "rb") as f:
    result = parse_blackbox_log(f)
    print(result['headers'])
    print(result['flight_data'][0])
```