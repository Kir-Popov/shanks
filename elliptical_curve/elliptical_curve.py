class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def copy(self):
        return Point(self.x, self.y)


class EllipticalCurve:
    """
    y^2 = x^3 + ax + b
    """

    def __init__(self, a, b, mod):
        self.a = a
        self.b = b
        self.mod = mod

    def multiply(self, p: Point, k: int) -> Point:
        result = Point(0, 0)
        base = p.copy()

        while k > 0:
            if k % 2 == 1:
                result = self.add(result, base)
            base = self.add(base, base)
            k //= 2

        return result


    def add(self, p: Point, q: Point) -> Point:
        if p.x == 0 and p.y == 0:
            return q.copy()
        if q.x == 0 and q.y == 0:
            return p.copy()

        if p.x != q.x:
            m = (p.y - q.y) * ((p.x - q.x) ** (self.mod - 2)) % self.mod
        else:
            m = (3 * (p.x * p.x) + self.a)*((2 * p.y) ** (self.mod - 2)) % self.mod

        xr = (m ** 2 - p.x - q.x) % self.mod
        yr = -(p.y + m * (xr - p.x)) % self.mod

        return Point(x=xr, y=yr)

