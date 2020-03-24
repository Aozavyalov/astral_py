class StandartIO:
    def input(self):
        return input()

    def output(self):
        pass

    def get_move(self):
        move_str = self.input() # must be like "caster spell target"
        return self.parse_move(move_str)

    def parse_move(self, move_str):
        move_str_parts = move_str.split()
        if len(move_str_parts) != 2 and len(move_str_parts) != 3 and not isinstance(move_str_parts[1], int):
            raise ValueError(f"Wrong move input!")
        return {move_str_parts[0]: {"spell": int(move_str_parts[1]),
                                    "target": None if len(move_str_parts) != 3 else move_str_parts[2]}}
