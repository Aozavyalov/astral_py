from utils import check_value

class BaseMagic:
    def __init__(self, time: int, idx: int, name: str, func: function):
        self._idx = idx
        self._time = time  # can't be changed after creating!
        self._name = name
        self._func = func

    @property
    def time(self):
        return self._time

    @property
    def name(self):
        return self._name

    def __call__(self, *args, **kwargs):
        return self._func(*args, **kwargs)

class Spell(BaseMagic):
    possible_targets = (
        "self",
        "ally",
        "enemy",
        "all"
    )
    spell_types = (
        "attack",
        "defence"
    )

    def __init__(self, idx: int, name: str, func: function,
                 priority: int, target: str, is_directed: bool, spell_type: str,
                 level: int, mana_req: int, mult_constant=10):
        super().__init__(time=mult_constant*priority, idx, name, func)

        check_value(priority, int, 'priority', priority >= 0)
        check_value(target, str, 'target', target in Spell.possible_targets)
        check_value(is_directed, bool, 'is_directed')
        check_value(spell_type, str, 'spell_type', spell_type in Spell.spell_types)
        check_value(level, int, 'level', level > 0 and level < 4)
        check_value(mana_req, int, 'mana_req', mana_req > 0)

        self._priority = priority
        self._target = target
        self._is_directed = is_directed
        self._type = spell_type
        self._level = level
        self._mana_req = mana_req

    @property
    def priority(self):
        return priority


class SimpleEffect(BaseMagic):
    def __init__(self, idx: int, time: int, name: str, func: function,
                 cast_group: int, is_dispelable: bool):
        super().__init__(time, idx, name, func)

        check_value(cast_group, int, 'cast_group', cast_group >= 0 and cast_group < 3)
        check_value(is_dispelable, int, 'is_dispelable', is_dispelable >= 0 and is_dispelable < 3)
        self._cast_group = cast_group  # can be 0, 1, 2
        self._is_dispelable = is_dispelable

class Effect(SimpleEffect):
    def __init__(self, idx: int, time: int, name: str, func: function,
                 cast_group: int, is_dispelable: bool, effects):
        super().__init__(idx, time, name, func, cast_group, is_dispelable)
        self._effects = list(effects)
