# IP Tracker (Python)

![Tool terminal screenshot](./Screenshot%202026-02-09%20174833.png)

A small, dependency-light command-line tool to fetch public information about IPv4 and IPv6 addresses using the ipapi.co public API.

## Features
- Query city, region, and country for an IP
- Latitude & longitude
- Timezone, ASN, ISP/organization
- Currency, language, and basic country statistics

## Requirements
- Python 3.8 or newer
- Internet connection
- Python package: `requests`

Install the required Python package:

```bash
pip install -r requirements.txt
```

## Installation
Clone the repository and change into the project folder:

```bash
git clone https://github.com/Kushdeveloper68/IP-tracker-tool-using-python.git
cd IP-tracker-tool-using-python
```

Ensure dependencies are installed (`requests`).

## Usage
Run the tool from the project directory:

```bash
python index.py
```

The script runs interactively and shows a small menu. Commands:

- `1` — help: shows the detailed help/usage screen
- `2` — trackip: prompt for an IP address to query
- `3` — exit: quit the tool

Example session:

```text
Enter a command (1, 2, 3): 2
Enter a IP address: 8.8.8.8
[*] Fetching information from IP address...
============================== IP INFORMATION START ==============================
IP INFORMATION: {'Ip Address': '8.8.8.8', 'city': 'Mountain View', ...}
=============================== IP INFORMATION END ===============================
```

Note: The tool prints a Python dictionary returned from the API. You can adapt the code in `index.py` to format output differently (e.g., table or JSON file).

## API, Rate Limits & Privacy
- This tool uses the ipapi.co free public API. Free-tier endpoints have rate limits and may return partial or throttled responses.
- Do not rely on the free service for production usage. For higher request volumes, use a paid API plan or host your own geolocation service.
- The tool only sends the queried IP to ipapi.co. Do not use the tool for illegal, abusive, or unethical purposes.

## Security & Ethical Use
This project is intended for legitimate, educational, and diagnostic uses only. By using this tool you agree to comply with all applicable laws and respect privacy. The author is not responsible for misuse.

## Troubleshooting
- If you see `Failed to fetch data from API` or HTTP errors, check your internet connection and API availability.
- If the script prints raw HTML or non-JSON responses, the API endpoint might have returned an error page — try again later or test with a different IP.
- If you see a `ModuleNotFoundError: No module named 'requests'`, install the `requests` package as shown above.

## Customization
- You can modify `index.py` to change output formatting, add CSV/JSON export, or integrate alternative geolocation APIs.

## Contributing
Feel free to open issues or pull requests. Suggested contributions:
- Add argument parsing to accept IPs via CLI flags
- Add structured JSON or CSV output
- Add unit tests and CI checks

## License
This README does not include a license file. If you want a permissive license, consider adding an `LICENSE` file (for example, MIT).

## Author
Made by: Developer Kush Pandit
Original repo: https://github.com/Kushdeveloper68/IP-tracker-tool-using-python

## Disclaimer
This tool is provided "as-is" without warranty. Use responsibly.
