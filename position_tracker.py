class PositionTracker:
    def __init__(self, x: int, y: int, facing: str):
        self._validate_facing(facing)
        self.x = x
        self.y = y
        self.facing = facing
    
    def _validate_facing(self, facing: str):
        if len(facing) != 1 or facing not in "NSEW":
            raise ValueError(f"Unexpected initial facing: {facing}")
