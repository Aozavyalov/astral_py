import logging

from Classes.Player import Player

class Team(set):
    def __init__(self, name, *players):
        super().__init__(*players)
        self._logger = logging.getLogger()
        self._name = name

    def __getitem__(self, player_name):
        for p in self:
            if p.name == player_name:
                return p
        raise KeyError(f"There is no player {player_name} in {self._name} team!")

    def __hash__(self):
        return hash(self._name)  # a name must be unique

    def __eq__(self, other):
        return isinstance(other, Team) and self._name == other.name

    def __repr__(self):
        return f"<{self._name}: {', '.join({p.name for p in self})}>"

    @property
    def name(self):
        return self._name

    def get_active(self):
        return {p for p in self if p.is_active}

    @staticmethod
    def create_team(name, players_names, hp, max_hp, mana):
        return Team(name, *{Player(name, health=hp, max_health=max_hp, mana=mana)})
