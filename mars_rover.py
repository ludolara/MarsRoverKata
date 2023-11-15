from command_handler import CommandHandler

class MarsRover:
    def __init__(self, command_handler: CommandHandler):
        self.command_handler = command_handler

    def __call__(self, commands: str) -> None:
        for character in commands:
            self.command_handler(character)
