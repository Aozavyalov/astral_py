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
        self.assertEqual(p.max_mana, 40)
        self.assertEqual(p._armor, 0)
        self.assertEqual(p._mana_regen, 1)
        self.assertEqual(p._damage_over_time, 0)
        with self.assertRaises(ValueError):
            Player("lol")
        Player.remove_name("lol")
        p = Player("lol", max_health=1)
        self.assertEqual(p._health, 1)
        self.assertEqual(p._mana, 8)
        self.assertEqual(p._max_health, 1)
        self.assertEqual(p.max_mana, 11)
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
        p = Player("lol", health=30)
        p.damage(16)
        self.assertEqual(p._health, 14)
        p.damage(10)
        self.assertEqual(p._health, 4)
        p.damage(14)
        self.assertEqual(p._health, -10)        
        with self.assertRaises(ValueError):
                p.damage(-1)    

    def test_next_round(self):
        pass

    def test_armor(self):
        p = Player("lol", health=30)
        p.add_armor(10)
        p.damage(10)
        self.assertEqual(p._health, 30)
        p.damage(25)
        self.assertEqual(p._health, 15)   
        with self.assertRaises(ValueError):
            p.add_armor(-1)

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
