import requests


FPL_URLS = {
    "fixtures": "https://fantasy.premierleague.com/api/fixtures/",
    "bulk": "https://fantasy.premierleague.com/api/bootstrap-static/",
    "gameweek_results": "https://fantasy.premierleague.com/api/event/GW/live/",
}

def get_fixtures():
    fixtures = requests.get(FPL_URLS["fixtures"])
    return fixtures.json()

def get_bulk_data():
    data = requests.get(FPL_URLS["bulk"])
    return data.json()


