from utility import epsilon_equal as ee


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other) -> bool:
        return ee(self.x, other.x) and ee(self.y, other.y)

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'

    def distance(self, to) -> float:
        return ((self.x - to.x) ** 2 + (self.y - to.y) ** 2) ** 0.5


class Circle:
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

    def __eq__(self, other) -> bool:
        return self.center == other.center and self.radius == other.radius

    def __ne__(self, other) -> bool:
        return not (self.center == other.center and
                    self.radius == other.radius)

    def __repr__(self) -> str:
        return f'{self.radius} @ ({self.center.x}, {self.center.y})'

    def overlaps(self, other) -> bool:
        sum_radii = self.radius + other.radius
        return sum_radii > self.center.distance(other.center)
