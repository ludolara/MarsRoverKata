import unittest
from position_tracker import PositionTracker
from command_handler import CommandHandler
from unittest.mock import Mock

class TestCommandHandler(unittest.TestCase):
    def setUp(self):
        self.mock_position_tracker = Mock(spec=PositionTracker)
        self.command_handler = CommandHandler(self.mock_position_tracker)

    def test_command_handler_with_forward_command_is_valid(self):
        self.command_handler("f")
        self.mock_position_tracker.move_forward.assert_called_once()

    def test_command_handler_with_backward_command_is_valid(self):
        self.command_handler("b")
        self.mock_position_tracker.move_backward.assert_called_once()

    def test_command_handler_with_left_command_is_valid(self):
        self.command_handler("l")

    def test_command_handler_with_right_command_is_valid(self):
        self.command_handler("r")

    def test_command_handler_with_empty_string_is_invalid(self):
        with self.assertRaisesRegex(ValueError, "Unexpected command"):
            self.command_handler("")

    def test_command_handler_with_invalid_command_is_invalid(self):
        with self.assertRaisesRegex(ValueError, "Unexpected command"):
            self.command_handler("x")

    def test_command_handler_with_integer_is_invalid(self):
        with self.assertRaisesRegex(ValueError, "Unexpected command"):
            self.command_handler(1)

    def test_command_handler_with_none_is_invalid(self):
        with self.assertRaisesRegex(ValueError, "Unexpected command"):
            self.command_handler(None)