from objects import Circle, Point


# Purpose: Return a list representing the distance of each point from origin.
def point_distance_all(points: list) -> list:
    return [(point.x ** 2 + point.y ** 2) ** 0.5 for point in points]


# Purpose: Filter out points that are not in the first quadrant.
def are_in_first_quadrant(points: list) -> list:
    return [p for p in points if p.x > 0 and p.y > 0]


# Purpose: Return center of each circle from the origin.
def circle_distance_all(circles: list) -> list:
    origin = Point(0, 0)
    return [c.center.distance(origin) for c in circles]


# Purpose: Return which circles overlap with the unit circle.
def overlaps_all(circles: list) -> list:
    unit_circle = Circle(Point(0, 0), 1)
    return [c for c in circles if c.overlaps(unit_circle)]
