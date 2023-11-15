from typing import Callable
from position_tracker import PositionTracker

class CommandHandler:
    def __init__(self, movement_map: PositionTracker):
        self.movement_map: dict[str, Callable] = {
            "f": movement_map.move_forward,
            "b": movement_map.move_backward,
            "l": None,
            "r": None,
        }

    def __call__(self, command: str):
        if not isinstance(command, str) or command not in self.movement_map:
            raise ValueError(f"Unexpected command '{command}'")
        
        execute_command: Callable = self.movement_map[command]
        if execute_command:
            execute_command()
