from requests import get
import sys
print("""
  ______  _______         ________                             __                                    __                          __ 
|      \|       \       |        \                           |  \                                  |  \                        |  |
 \$$$$$$| $$$$$$$\       \$$$$$$$$______   ______    _______ | $$   __   ______    ______         _| $$_     ______    ______  | $$
  | $$  | $$__/ $$         | $$  /      \ |      \  /       \| $$  /  \ /      \  /      \       |   $$ \   /      \  /      \ | $$
  | $$  | $$    $$         | $$ |  $$$$$$\ \$$$$$$\|  $$$$$$$| $$_/  $$|  $$$$$$\|  $$$$$$\       \$$$$$$  |  $$$$$$\|  $$$$$$\| $$
  | $$  | $$$$$$$          | $$ | $$   \$$/      $$| $$      | $$   $$ | $$    $$| $$   \$$        | $$ __ | $$  | $$| $$  | $$| $$
 _| $$_ | $$               | $$ | $$     |  $$$$$$$| $$_____ | $$$$$$\ | $$$$$$$$| $$              | $$|  \| $$__/ $$| $$__/ $$| $$
|   $$ \| $$               | $$ | $$      \$$    $$ \$$     \| $$  \$$\ \$$     \| $$               \$$  $$ \$$    $$ \$$    $$| $$
 \$$$$$$ \$$                \$$  \$$       \$$$$$$$  \$$$$$$$ \$$   \$$  \$$$$$$$ \$$                \$$$$   \$$$$$$   \$$$$$$  \$$
                                                                                                                                   
                                                                                                                                   
                                                                                                                                   """)
print("Made by: developer kush pandit")
print("github: https://gtihub.com/kushdeveloper68")

def trackip(ip): 
        data = get(f'https://ipapi.co/{ip}/json/')
        response = data.json()
        
        if data.status_code != 200:
           print("\033[91m[!] Failed to fetch data from API\033[0m")
           sys.exit()

        try:
           response = data.json()
        except ValueError:
           print("\033[91m[!] Invalid response received (not JSON)\033[0m")
           print(data.text)
           sys.exit()

        location_data = {
                    "Ip Address": ip,
                    "city": response.get("city"),
                    "region": response.get("region"),
                    "country": response.get("country_name"),
                    "Ip Address Type": response.get("version"),
                    "Region Code": response.get("region_code"),
                    "Postal Code": response.get("postal"),
                    "Latitude": response.get(str("latitude")),
                    "Longitude": response.get(str("longitude")),
                    "TimeZone": response.get("timezone"),
                    "Country code": response.get("country_calling_code"),
                    "Currency": response.get("currency"),
                    "Currency Name": response.get("currency_name"),
                    "Languages": response.get("languages"),
                    "Country Area": response.get("country_area"),
                    "Population": response.get("country_population"),
                    "ASN": response.get("asn"),
                    "Organization": response.get("org")
                }
        return location_data


print("\033[95m" + "="*98 + "\033[0m")
print("""
\033[96mAll Commands:\033[0m

\033[92m[1]\033[97m help
\033[92m[2]\033[97m trackip
\033[92m[3]\033[97m exit
""")

print("\033[93mEnter a command (1, 2, 3):\033[0m", end=" ")

command = input()

if command == "1":
    print("\033[96m"
"""
██╗  ██╗███████╗██╗     ██████╗     ███╗   ███╗███████╗███╗   ██╗██╗   ██╗
██║  ██║██╔════╝██║     ██╔══██╗    ████╗ ████║██╔════╝████╗  ██║██║   ██║
███████║█████╗  ██║     ██████╔╝    ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
██╔══██║██╔══╝  ██║     ██╔═══╝     ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
██║  ██║███████╗███████╗██║         ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
╚═╝  ╚═╝╚══════╝╚══════╝╚═╝         ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ 

\033[93mTool Name : IP TRACKER
Author    : Developer Kush Pandit

\033[97mDescription:
This tool fetches public information of any IPv4 or IPv6 address
using the ipapi.co public API.

\033[92mAvailable Commands:

  [1] help
      Show help menu and usage instructions

  [2] trackip
      Track an IP address and fetch:
        • City / Region / Country
        • Latitude & Longitude
        • Timezone
        • ISP / Organization
        • ASN, Currency, Languages

  [3] exit
      Exit the tool safely

\033[94mUsage Example:

  Select Command : 2
  Enter IP       : 8.8.8.8

\033[91mNotes:
  • Internet connection required
  • Free API has rate limits
  • For educational & ethical use only

════════════════════════════════════════════════════════════════════════════
\033[0m
"""
)

elif command == "2":
    ipAddress = input("Enter a IP address:")
    print("\033[94m[*] Fetching information from IP address...\033[0m")
    print("\033[92m" + "="*30 + " IP INFORMATION START " + "="*30 + "\033[0m")
    print("""IP INFORMATION:""", trackip(ipAddress))
    print("\033[92m" + "="*31 + " IP INFORMATION END " + "="*31 + "\033[0m")
else:
    print("\033[91mThanks for coming... exiting.\033[0m")
    exit()