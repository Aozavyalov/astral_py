import logging

from Classes.Team import Team

class Game:
    def __init__(self, teams_num=2, players_in_team=1, start_hp=30, start_mp=30, rounds_num=30):
        self._logger = logging.getLogger()
        self._teams = create_teams(teams_num, players_in_team, start_hp, start_mp)
        self._rounds_num = rounds_num

    def create_teams(teams_num, players_in_team, start_hp, start_mp):
        teams = set()
        for i in range(teams_num):
            team_name = input(f"Input team's name or it will be a number:")
            team_name = f"Team {i+1}" if not team_name else team_name
            players_names = set()
            for _ in range(players_in_team):
                players_names.add(input("Input player's name:"))
            teams.add(Team(team_name, players_names, start_hp, start_mp))
        return teams

    def start(self):
        # start of the game
        for i in range(self._rounds_num):
            # get all moves
            # precast time
            # cast time
            # aftercast time
            # check if there is one alive team
            pass
        # end of the game
