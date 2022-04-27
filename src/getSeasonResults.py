from datetime import date
from src import getRaceResult


def getSeasonResults():
    races_result = []
    current_year = date.today().year
    for round in range(1, 25):
        try:
            race_result = getRaceResult(current_year, round)
            races_result.append(race_result)
        except IndexError:
            break
    return races_result
