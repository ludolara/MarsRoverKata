import unittest
from planet import Planet

class TestPlanetInitialState(unittest.TestCase):
    def setUp(self):
        self.planet = Planet(3,3)

    def test_planet_width_given_initial_width(self):
        self.assertEqual(self.planet.width, 3)

    def test_planet_height_given_initial_height(self):
        self.assertEqual(self.planet.width, 3)
    
    def test_planet_initial_map(self):
        expected_map = [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]
        ]
        self.assertEqual(self.planet.map, expected_map)

class TestPlanetWithObstacle(unittest.TestCase):
    def setUp(self):
        self.width = 3
        self.height = 3
        self.planet = Planet(self.width,self.height)

    def test_planet_add_obstacle(self):
        self.planet.add_obstacle(1, 1)
        expected_map_with_obstacle = [
            ["-", "-", "-"],
            ["-", "*", "-"],
            ["-", "-", "-"]
        ]
        self.assertEqual(self.planet.map, expected_map_with_obstacle)
