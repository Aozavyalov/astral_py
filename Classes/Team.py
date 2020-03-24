import logging

from Classes.Player import Player

class Team:
    def __init__(self, name, players_names, start_hp, start_mp):
        self._logger = logging.getLogger()
        self._name = name
        self._players = set()
        for name in players_names:
            self._players.add(Player(name, max_health=start_hp, mana=start_mp))

    def __getitem__(self, player_name):
        for p in self._players:
            if p.name == player_name:
                return p
        raise KeyError(f"There is no player {player_name} in {self._name} team!")

    def __len__(self):
        return len(self._players)

    def __contains__(self, player_name):
        for p in self._players:
            if p.name == player_name:
                return True
        return False

    def get_names(self):
        return {p.name for p in self._players]}

    def get_alive_players_names(self):
        return {p.name for p in self._players if p.is_alive}
