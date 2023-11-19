from elliptical_curve import EllipticalCurve, Point


def test():
    ec = EllipticalCurve(a=2, b=3, mod=97)

    points = set()
    p = Point(3, 6)

    current_point = Point(0, 0)
    while True:
        if current_point in points:
            break
        points.add(current_point)

        current_point = ec.add(current_point, p)
    print(points)


if __name__ == '__main__':
    test()

