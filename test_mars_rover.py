import unittest
from mars_rover import MarsRover
from position_tracker import PositionTracker
from command_handler import CommandHandler

class TestMarsRover(unittest.TestCase):
    def setUp(self):
        position_tracker = PositionTracker(0,0,"N")
        command_handler = CommandHandler(position_tracker)
        self.rover = MarsRover(command_handler)

    def test_command_handler_with_multiple_valid_commands_is_valid(self):
        self.rover("ffbbllrr")

    def test_command_handler_with_multiple_invalid_commands_is_invalid(self):
        with self.assertRaisesRegex(ValueError, "Unexpected command"):
            self.rover("xyz")

    def test_command_handler_with_multiple_int_commands_is_invalid(self):
        with self.assertRaisesRegex(ValueError, "Unexpected command"):
            self.rover([111])
