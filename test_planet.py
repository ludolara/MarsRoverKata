import unittest
from planet import Planet

class TestPlanetInitialState(unittest.TestCase):
    def setUp(self):
        self.planet = Planet(3,3)

    def test_planet_width_given_initial_width(self):
        self.assertEqual(self.planet.width, 3)

    def test_planet_height_given_initial_height(self):
        self.assertEqual(self.planet.width, 3)
