import requests
import json

def get_scoreboard():
    return requests.get("http://dvc.tf/api/v1/scoreboard").json()

dvctf_scoreboard = get_scoreboard()

"""
CTFtime format:
    {
        "standings": [
            { "pos": 1, "team": "Intergalactic Pwners", "score": 1700 },
            { "pos": 2, "team": "DaVinciCode", "score": 1699 }
        ]
    }
"""

ctftime_scoreboard = {"standings": []}

for i in dvctf_scoreboard["data"]:
    team = {}
    team["pos"] = i["pos"]
    team["team"] = i["name"]
    team["score"] = i["score"]
    ctftime_scoreboard["standings"].append(team)

with open('scoreboard.json', 'w') as output:
    json.dump(ctftime_scoreboard, output)
