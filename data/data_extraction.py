import datetime
from .fpl_requests import get_bulk_data, get_fixtures


class DataExtractor():

    def __init__(self) -> None:
        self.data = get_bulk_data()
        self.fixtures = get_fixtures()
        self.team_id_to_team_name()
    
    def show_teams(self):
        for team in self.data["teams"]:
            print(f"{team['name']} --- {team['id']}")
    
    def team_id_to_team_name(self):
        rtn = {}
        for team in self.data["teams"]:
            rtn[team["id"]] = team["name"]
        self.id_to_team = rtn
        return rtn
    
    def show_players(self):
        for player in self.data["elements"]:
            print(f"{player['first_name']} {player['second_name']} --- {self.id_to_team[player['team']]}")
        
    def show_fixtures_for_team(self, team_id: int):
        team_fixtures = []
        for fixture in self.fixtures:
            home = fixture["team_h"]
            away = fixture["team_a"]
            date = datetime.datetime.fromisoformat(fixture["kickoff_time"][:-1] + '+00:00')
            if team_id in (home, away):
                is_home = home == team_id
                if is_home:
                    win_prob = fixture["team_a_difficulty"] / fixture["team_h_difficulty"]
                else:
                    win_prob = fixture["team_h_difficulty"] / fixture["team_a_difficulty"]
                team_fixtures.append(fixture)
                print(f"{self.id_to_team[home]} vs {self.id_to_team[away]} on {date.strftime('%m/%d/%Y, %H:%M:%S')} win factor: {win_prob}")
        return team_fixtures