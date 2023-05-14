import webbrowser
import requests
import sys

url = "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json"

try:
    response = requests.get(url)
    if response.status_code == 200:
        webbrowser.open_new(url)
    else:
        print("Błąd kodu HTTP: ", response.status_code)
        sys.exit()

except requests.exceptions as e:
    print("Błąd: ", e)
    sys.exit()
