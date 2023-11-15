import unittest
from planet import Planet
from position_tracker import PositionTracker

class TestPositionTrackerInitialState(unittest.TestCase):
    def setUp(self):
        self.planet = Planet(3,3)
        self.position_tracker = PositionTracker(1,2,"N",self.planet)

    def test_position_x_given_initial_x(self):
        self.assertEqual(self.position_tracker.x, 1)

    def test_position_y_given_initial_y(self):
        self.assertEqual(self.position_tracker.y, 2)

    def test_facing_given_valid_initial_facing(self):
        self.assertEqual(self.position_tracker.facing, "N")

    def test_facing_given_invalid_initial_facing(self):
        with self.assertRaisesRegex(ValueError, "Unexpected initial facing: A"):
            self.position_tracker = PositionTracker(1,2,"A", self.planet)
