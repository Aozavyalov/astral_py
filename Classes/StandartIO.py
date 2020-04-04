class StandartIO:
    def input(self, in_string=None):
        if in_string:
            print(in_string)
        return input()

    def output(self):
        pass

    def get_move(self):
        move_str = self.input() # must be like "caster spell target"
        return self.parse_move(move_str)

    def parse_move(self, move_str):
        move_str_parts = move_str.split()
        if (len(move_str_parts) == 2 or len(move_str_parts) == 3) and move_str_parts[1].isdigit():
            return move_str_parts[0], int(move_str_parts[1]), None if len(move_str_parts) != 3 else move_str_parts[2]
        raise ValueError(f"Wrong move input!")
