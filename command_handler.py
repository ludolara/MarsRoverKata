from typing import Callable

class CommandHandler:
    def __init__(self, movement_map: dict[str, Callable]):
        self.movement_map: dict[str, Callable] = {
            "f": None,
            "b": None,
            "l": None,
            "r": None,
        }

    def __call__(self, command: str):
        if not isinstance(command, str) or command not in self.movement_map:
            raise ValueError(f"Unexpected command '{command}'")

