import webbrowser
import requests
import sys

url = "https://httpbin.org/delay/2"

caption = {"Content-Type: application/json"}

try:
    response = requests.get(url, timeout=1)
    if response.status_code == 200:
        webbrowser.open_new(url)
    else:
        print("Błąd kodu HTTP: ", response.status_code)
        sys.exit()

except requests.exceptions as e:
    print("Błąd: ", e)
    sys.exit()
