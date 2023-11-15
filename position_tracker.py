class PositionTracker:
    def __init__(self, x: int, y: int, facing: str):
        self._validate_facing(facing)
        self.x = x
        self.y = y
        self.facing = facing
        self.offset_map = {
            "N": (0, 1),
            "E": (1, 0),
            "S": (0, -1),
            "W": (-1, 0)
        }
        self.compass = list(self.offset_map.keys())
    
    def _validate_facing(self, facing: str):
        if len(facing) != 1 or facing not in "NSEW":
            raise ValueError(f"Unexpected initial facing: {facing}")
    
    @property
    def offset(self) -> list[int]:
        direction: str = self.facing
        return self.offset_map[direction]
    
    @property
    def facing_int(self) -> int:
        facing_int: int = self.compass.index(self.facing)
        return facing_int
    
    def move_forward(self) -> None:
        self.x += self.offset[0]
        self.y += self.offset[1]

    def move_backward(self) -> None:
        self.x -= self.offset[0]
        self.y -= self.offset[1]
    
    def turn_left(self) -> None:
        self.facing = self.compass[(self.facing_int - 1) % len(self.compass)]
    
    def turn_right(self) -> None:
        self.facing = self.compass[(self.facing_int + 1) % len(self.compass)]
