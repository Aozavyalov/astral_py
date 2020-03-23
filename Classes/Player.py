import logging

from Classes.utils import check_int_args, check_value


class Player:
    _names = set()
    def __init__(self, name, **kwargs):
        self._logger = logging.getLogger()  # create a logger
        # check if a player with this name is exists
        if name in Player._names:
            raise ValueError(f"The name {name} already exists!")
        check_value(name, str, 'name', len(name) > 1)
        self._name = name
        # max health setting
        self._max_health = kwargs.get("max_health", 30)
        check_value(self._max_health, int, 'max_health', self._max_health > 0)
        # max mana setting
        self._max_mana = kwargs.get("max_mana", 30)
        check_value(self._max_mana, int, 'max_mana', self._max_mana > 0)
        # health setting
        self._health = kwargs.get("health", self._max_health)
        check_value(self._health, int, 'health', self._health > 0 and self._health <= self._max_health)
        # mana setting
        self._mana = kwargs.get("mana", self._max_mana)    
        check_value(self._mana, int, 'mana', self._mana <= self._max_mana)
        # armor setting
        self._armor = kwargs.get("armor", 0)
        check_value(self._armor, int, 'armor', self._armor >= 0)
        # mana regen setting
        self._mana_regen = kwargs.get("mana_regen", 1)
        check_value(self._mana_regen, int, 'mana_regen', self._mana_regen >= 0)
        # DOT setting
        self._damage_over_time = kwargs.get("damage_over_time", 0)
        check_value(self._damage_over_time, int, 'damage_over_time', self._damage_over_time >= 0)
        Player._names.add(name)  # after all checks save players name
        self._effects = list()  # [{"idx": effect_idx, "until_end": rounds_until_end, "dispelable": is_dispelable}, ...]
        self._spells = dict()  # {spell_idx: num_of_that_spells, ...}

    def kill(self):
        self._health = 0

    @property
    def is_alive(self):
        return self._health > 0

    def reborn(self, health):
        self._health = health
        if self._max_health < health:
            self._max_health = health

    @check_int_args
    def heal(self, val):
        self._health += val
        self._health = self._max_health if self._max_health < self._health else self._health

    @check_int_args
    def damage(self, val):
        damage_with_armor = val - self._armor
        self._health -= damage_with_armor if damage_with_armor > 0 else 0

    @check_int_args
    def add_max_health(self, val):
        self._max_health += val

    @check_int_args
    def sub_max_health(self, val):
        self._max_health -= val

    @check_int_args
    def add_armor(self, val):
        self._armor += val

    def remove_armor(self):
        self._armor = 0

    def next_round(self):
        if self.is_alive:
            self._mana += self._mana_regen
            self._health -= self._damage_over_time
            self._health += self._mana if self._mana < 0 else 0
            removed = 0
            for i in range(len(self._effects)):  # decrease counters for ending
                if self._effects[i-removed]['ends'] == 0:
                    del self._effects[i-removed]
                    removed += 1
                else:
                    self._effects[i-removed]['ends'] -= 1
        else:
            self._spells = dict()
            self._effects = list()

    @classmethod
    def remove_name(cls, name):
        if name in cls._names:
            cls._names.remove(name)
