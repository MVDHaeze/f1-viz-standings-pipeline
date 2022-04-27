import requests
import json


def getRaceResult(year, round):
    url = f"http://ergast.com/api/f1/{year}/{round}/results.json"

    res = requests.get(url)
    response = json.loads(res.text)
    races = response["MRData"]["RaceTable"]["Races"]
    for result in races:
        drivers = result["Results"]

    keys_to_keep = ["season", "round", "raceName"]
    race_result = {key: races[0][key] for key in keys_to_keep}

    drivers_result = []
    keys_to_keep = ["number", "position", "points", "Driver"]
    for driver in drivers:
        driver_result = {key: driver[key] for key in keys_to_keep}
        driver_result["Driver"] = driver_result["Driver"]["driverId"]
        drivers_result.append(driver_result)

    race_result["result"] = drivers_result
    return race_result
