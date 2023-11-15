import unittest
from mars_rover import MarsRover
from planet import Planet
from position_tracker import PositionTracker
from command_handler import CommandHandler

class TestMarsRover(unittest.TestCase):
    def setUp(self):
        self.planet = Planet(3,3)
        self.position_tracker = PositionTracker(1,1,"N",self.planet)
        self.command_handler = CommandHandler(self.position_tracker)
        self.rover = MarsRover(self.command_handler)

    def test_command_handler_with_multiple_valid_commands_is_valid(self):
        self.rover("bfflrr")
        self.assertEqual(self.position_tracker.y, 2)
        self.assertEqual(self.position_tracker.facing, "E")

    def test_command_handler_with_multiple_invalid_commands_is_invalid(self):
        with self.assertRaisesRegex(ValueError, "Unexpected command"):
            self.rover("xyz")

    def test_command_handler_with_multiple_int_commands_is_invalid(self):
        with self.assertRaisesRegex(ValueError, "Unexpected command"):
            self.rover([111])

    def test_move_forward_from_north(self):
        self.rover("f")
        self.assertEqual(self.position_tracker.y, 2)

    def test_move_backward_from_north(self):
        self.rover("b")
        self.assertEqual(self.position_tracker.y, 0)

    def test_move_forward_from_east(self):
        self.position_tracker.facing = "E"
        self.rover("f")
        self.assertEqual(self.position_tracker.x, 2)

    def test_move_backward_from_east(self):
        self.position_tracker.facing = "E"
        self.rover("b")
        self.assertEqual(self.position_tracker.x, 0)

    def test_move_forward_from_south(self):
        self.position_tracker.facing = "S"
        self.rover("f")
        self.assertEqual(self.position_tracker.y, 0)

    def test_move_backward_from_south(self):
        self.position_tracker.facing = "S"
        self.rover("b")
        self.assertEqual(self.position_tracker.y, 2)

    def test_move_forward_from_west(self):
        self.position_tracker.facing = "W"
        self.rover("f")
        self.assertEqual(self.position_tracker.x, 0)

    def test_move_backward_from_west(self):
        self.position_tracker.facing = "W"
        self.rover("b")
        self.assertEqual(self.position_tracker.x, 2)

    def test_turn_right_from_north_to_east(self):
        self.rover("r")
        self.assertEqual(self.position_tracker.facing, "E")

    def test_turn_right_from_east_to_south(self):
        self.position_tracker.facing = "E"
        self.rover("r")
        self.assertEqual(self.position_tracker.facing, "S")

    def test_turn_right_from_south_to_west(self):
        self.position_tracker.facing = "S"
        self.rover("r")
        self.assertEqual(self.position_tracker.facing, "W")

    def test_turn_right_from_west_to_north(self):
        self.position_tracker.facing = "W"
        self.rover("r")
        self.assertEqual(self.position_tracker.facing, "N")

    def test_turn_left_from_north_to_west(self):
        self.rover("l")
        self.assertEqual(self.position_tracker.facing, "W")

    def test_turn_left_from_west_to_south(self):
        self.position_tracker.facing = "W"
        self.rover("l")
        self.assertEqual(self.position_tracker.facing, "S")

    def test_turn_left_from_south_to_east(self):
        self.position_tracker.facing = "S"
        self.rover("l")
        self.assertEqual(self.position_tracker.facing, "E")

    def test_turn_left_from_east_to_north(self):
        self.position_tracker.facing = "E"
        self.rover("l")
        self.assertEqual(self.position_tracker.facing, "N")

    def test_rover_facing_north_wraps_from_north_to_south_edge_moving_backward_from_origin(self):
        self.position_tracker.x, self.position_tracker.y = 0,0
        self.rover("b")
        self.assertEqual(self.position_tracker.y, self.planet.height-1)

    def test_rover_facing_south_wraps_from_south_to_north_edge_moving_forward_from_origin(self):
        self.position_tracker.x, self.position_tracker.y = 0,0
        self.position_tracker.facing = "S"
        self.rover("f")
        self.assertEqual(self.position_tracker.y, self.planet.height-1)

    def test_rover_facing_east_wraps_from_east_to_west_edge_moving_backward_from_origin(self):
        self.position_tracker.x, self.position_tracker.y = 0,0
        self.position_tracker.facing = "E"
        self.rover("b")
        self.assertEqual(self.position_tracker.x, self.planet.width-1)

    def test_rover_facing_west_wraps_from_west_to_east_edge_moving_forward_from_origin(self):
        self.position_tracker.x, self.position_tracker.y = 0,0
        self.position_tracker.facing = "W"
        self.rover("f")
        self.assertEqual(self.position_tracker.x, self.planet.width-1)
