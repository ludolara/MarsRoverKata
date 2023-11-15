from planet import Planet

class ObstacleDetected(Exception):
    def __init__(self, x, y, message="Obstacle detected"):
        self.x = x
        self.y = y
        self.message = f"{message} at position ({x}, {y})"
        super().__init__(self.message)
class PositionTracker:
    def __init__(self, x: int, y: int, facing: str, planet: Planet):
        self._validate_facing(facing)
        self.x = x
        self.y = y
        self.facing = facing
        self.planet = planet
        self.offset_map = {
            "N": (0, 1),
            "E": (1, 0),
            "S": (0, -1),
            "W": (-1, 0)
        }
        self.compass = list(self.offset_map.keys())
    
    @property
    def offset(self) -> list[int]:
        direction: str = self.facing
        return self.offset_map[direction]
    
    @property
    def facing_int(self) -> int:
        facing_int: int = self.compass.index(self.facing)
        return facing_int
    
    def move_forward(self) -> None:
        new_x = (self.x + self.offset[0]) % self.planet.width
        new_y = (self.y + self.offset[1]) % self.planet.height
        self._obstacle_detector(new_x, new_y)
        self.x, self.y = new_x, new_y

    def move_backward(self) -> None:
        new_x = (self.x - self.offset[0]) % self.planet.width
        new_y = (self.y - self.offset[1]) % self.planet.height
        self._obstacle_detector(new_x, new_y)
        self.x, self.y = new_x, new_y

    def turn_left(self) -> None:
        self.facing = self.compass[(self.facing_int - 1) % len(self.compass)]
    
    def turn_right(self) -> None:
        self.facing = self.compass[(self.facing_int + 1) % len(self.compass)]
    
    def _obstacle_detector(self, x: int, y: int) -> None:
        if self.planet.map[y][x] == "*":
            raise ObstacleDetected(x,y)
    
    def _validate_facing(self, facing: str):
        if len(facing) != 1 or facing not in "NSEW":
            raise ValueError(f"Unexpected initial facing: {facing}")
