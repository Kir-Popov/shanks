from shanks import gelfond_shanks
from elliptical_curve import EllipticalCurve, Point


def test():
    a = 2
    b = 3
    mod = 17
    curve = EllipticalCurve(a, b, mod)

    p = Point(5, 6)
    q = curve.multiply(p, 8)  # Вычисляем Q = 7P

    result = gelfond_shanks(curve, p, q)
    print("Логарифм:", result)


if __name__ == '__main__':
    test()

