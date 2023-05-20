import webbrowser
import json

def superhero():
    with webbrowser.open(
            "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json") as response:
        body = response.read()

    inside = json.loads(body)

    names = [hero["name"] for hero in inside["squadName"]]

    for name in names:
        print(name)

superhero()
