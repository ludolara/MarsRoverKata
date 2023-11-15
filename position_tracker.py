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
    
    def _validate_facing(self, facing: str):
        if len(facing) != 1 or facing not in "NSEW":
            raise ValueError(f"Unexpected initial facing: {facing}")
    
    @property
    def offset(self) -> list[int]:
        direction: str = self.facing
        return self.offset_map[direction]
    
    def move_forward(self) -> None:
        self.x += self.offset[0]
        self.y += self.offset[1]

    def move_backward(self) -> None:
        self.x -= self.offset[0]
        self.y -= self.offset[1]
