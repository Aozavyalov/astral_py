import unittest

from Classes.Player import Player

class PlayerTest(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(TypeError):
            Player()
        p = Player("lol")
        self.assertEqual(p._name, "lol", f"Wrong name {p._name}!")
        self.assertEqual(p._health, 30)
        self.assertEqual(p._mana, 30)
        self.assertEqual(p._max_health, 30)
        self.assertEqual(p._max_mana, 40)
        self.assertEqual(p._armor, 0)
        self.assertEqual(p._mana_regen, 1)
        self.assertEqual(p._damage_over_time, 0)
        with self.assertRaises(ValueError):
            Player("lol")
        Player.remove_name("lol")
        p = Player("lol", max_health=1)
        self.assertEqual(p._health, 1)
        self.assertEqual(p._mana, 1)
        self.assertEqual(p._max_health, 1)
        self.assertEqual(p._max_mana, 11)
        Player.remove_name("lol")
        p = Player("lol", health=1, mana=1)
        self.assertEqual(p._health, 1)
        self.assertEqual(p._mana, 1)

    def tearDown(self):
        Player.remove_name("lol")

    def test_healing(self):
        p = Player("lol", health=1)
        p.heal(10)
        self.assertEqual(p._health, 11)
        p.heal(100)
        self.assertEqual(p._health, 30)
        with self.assertRaises(ValueError):
            p.heal(-1)

    def test_damaging(self):
        pass

    def test_next_round(self):
        pass

    def test_armor(self):
        pass

    def test_mana(self):
        pass

    def test_kill(self):
        p = Player("lol")
        self.assertTrue(p.is_alive)
        p.sub_max_health(5)
        p.kill()
        self.assertFalse(p.is_alive)
        p.reborn(30)
        self.assertTrue(p.is_alive)
        self.assertEqual(p._health, 30)
        self.assertEqual(p._max_health, 30)
