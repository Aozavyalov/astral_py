import logging

from Classes.spells import SPELLS
from Classes.StandartIO import StandartIO
from Classes.Team import Team


class Game:
    def __init__(self, teams_num=2, players_in_team=1,
                 start_hp=30, start_mp=30, rounds_num=30,
                 io_cls=StandartIO):
        self._logger = logging.getLogger()
        self._teams = create_teams(teams_num, players_in_team, start_hp, start_mp)
        self._rounds_num = rounds_num
        self._io = io_cls()  # an object for input and output. Can be changed

    def create_teams(teams_num, players_in_team, start_hp, start_mp):
        # teams is a set with objects Team
        teams = set()
        for i in range(teams_num):
            # getting a name of a team. If pass it, it will be "Team №"
            team_name = input(f"Input team's name or it will be a number:")
            team_name = f"Team {i+1}" if not team_name else team_name
            # getting names for players from this team
            players_names = set()
            for _ in range(players_in_team):
                players_names.add(input("Input player's name:"))
            # create and save a new team
            teams.add(Team(team_name, players_names, start_hp, start_mp))
        return teams

    def start(self):
        # start of the game
        for i in range(self._rounds_num):
            # get all moves
            moves = self.get_moves()
            # precast time
            # cast time
            # aftercast time
            # check if there is one alive team
        # end of the game

    def get_moves(self):
        moves = set()
        alive_names = {t.get_alive_players_names() for t in self._teams}
        all_names = {t.get_names() for t in self._teams}
        while set(moves.keys()) != alive_names:
            # getting a move
            try:
                move = self._io.get_move()
            except ValueError as e:
                # TODO: add output
                print(e)
                continue
            # check if it is correct
            caster = next(iter(move))
            if not caster in alive_names:
                print(f"Wrong caster's name {caster}")
                continue
            elif move[caster]['spell'] not in SPELLS:
                print(f"There is no spell {move[caster]['spell']}")
                continue
            elif move[caster]['target'] and move[caster]['target'] not in all_names:  # TODO: add mass spell check
                print(f"Wrong target's name {move[caster]['target']}")
                continue
            else:
                moves.update(move)
        return moves