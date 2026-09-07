
import requests
import time

from test_telegram import send_message

rectangles = [
    {
        "x1":17,
        "z1":336,
        "x2":300,
        "z2":600
    }
]

def inside_rectangle(x, z, rect):
    return (
        rect["x1"] <= x <= rect["x2"]
        and
        rect["z1"] <= z <= rect["z2"]
    )


def inside_territory(x, z):
    for rect in rectangles:
        if inside_rectangle(x, z, rect):
            return True

    return False

def is_inside(x, z):
    return (x >= 17 and x <= 300) and (z >= 336 and z <= 600)

URL = "http://hollowvanilla.xyz:25590/maps/world/live/players.json"



previous_inside = {}

while(True):
    response = requests.get(URL, timeout=10)
    data = response.json()

    current_inside = {}

    for player in data["players"]:
        name = player["name"]
        pos = player["position"]
        x = pos["x"]
        y = pos["y"]
        z = pos["z"]
        print(
            name,
            "X:", pos["x"],
            "Y:", pos["y"],
            "Z:", pos["z"]
        )

        if inside_territory(pos["x"], pos["z"]):
            current_inside[name] = {
                "x": x,
                "y": y,
                "z": z
            }
    entered = current_inside.keys() - previous_inside.keys()
    left = previous_inside.keys() - current_inside.keys()

    for player in entered:
        pos = current_inside[name]

        send_message(
            f"🚨 Игрок вошёл на территорию!\n\n"
            f"👤 {name}\n"
            f"📍 X: {pos['x']:.0f}, "
            f"Y: {pos['y']:.0f}, "
            f"Z: {pos['z']:.0f}"
        )

    for player in left:
        send_message(
            f"✅ {player} покинул нашу территорию."
        )

    previous_inside = current_inside
    time.sleep(5)
