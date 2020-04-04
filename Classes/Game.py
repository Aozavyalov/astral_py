import logging

from Classes.spells import SPELLS
from Classes.StandartIO import StandartIO
from Classes.Team import Team


class Game:
    def __init__(self, teams_num=2, players_in_team=1,
                 start_hp=30, start_mp=30, max_hp=30, rounds_num=30,
                 io_cls=StandartIO):
        self._logger = logging.getLogger()
        self._io = io_cls()  # an object for input and output. Can be changed
        self._teams = self.create_teams(teams_num, players_in_team, start_hp, max_hp, start_mp)
        self._rounds_num = rounds_num

    def create_teams(self, teams_num: int, players_in_team: int, start_hp: int, max_hp: int, start_mp: int):
        teams = set()  # teams is a set with objects Team
        for i in range(teams_num):
            # getting a name of a team. If pass it, it will be "Team №"
            team_name = self._io.input(f"Input team's name or it will be a number:")
            team_name = f"Team {i+1}" if not team_name else team_name
            # getting names for players from this team
            players_names = set()
            for _ in range(players_in_team):
                players_names.add(input("Input player's name:"))
            # create and save a new team
            teams.add(Team.create_team(team_name, players_names, start_hp, max_hp, start_mp))
        return teams

    def start(self):
        # start of the game
        for i in range(self._rounds_num):
            # get all moves
            moves = self.get_moves()
            print(moves)
            # precast time
            # cast time
            # aftercast time
            # check if there is one alive team
        # end of the game

    def get_moves(self):
        moves = dict()
        all_names = self.get_players_names()
        active_names = self.get_players_names(True)
        while {*moves} != active_names:
            # getting a move
            try:
                caster, spell, target = self._io.get_move()
            except ValueError as e:
                # TODO: add output
                print(e)
                continue
            # TODO: add autotarget
            # check caster
            if caster not in all_names:
                print(f"Caster {caster} doesn't exist")
            elif caster not in active_names:
                print(f"Caster {caster} can't move now")
            # check spell
            elif spell not in SPELLS:
                print(f"There is no spell {spell}")
            # TODO: check target
            else:
                moves[caster] = {"spell": spell, "target" : target}
        return moves

    def get_players_names(self, only_active=False):
        """Returns names of all players. If only_active is True, returns names for active players.
        
        Args:
            only_active (bool, optional): If it is True, returns only names of active players. Defaults to False.
        
        Returns:
            set: Names of players from all teams.
        """
        names = set()
        for t in self._teams:
            names.update({p.name for p in t if not only_active or (only_active and p.is_active)})
        return names
