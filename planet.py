class Planet():
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.map = [["-" for _ in range(width)] for _ in range(height)]

    def add_obstacle(self, x, y):
        self.map[y][x] = "*"
