import urllib.requestss
import json

url = "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json"

try:
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
        print(data)
except urllib.error.HTTPError as e:
    print("Błąd kodu HTTP: ", e.code)
except urllib.error.URLError as e:
    print("Błąd URL: ", e.reason)
except json.JSONDecodeError as e:
    print("Błąd dekodowania JSON: ", e.msg)
