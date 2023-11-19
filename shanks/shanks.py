from elliptical_curve import EllipticalCurve, Point


def gelfond_shanks(curve: EllipticalCurve, p: Point, q: Point) -> int:
    m = int((curve.mod - 1) ** 0.5) + 1

    # Предварительное вычисление
    l1 = {curve.multiply(p, i): i for i in range(m)}

    _p = curve.multiply(p, m)
    for j in range(m):

        jp = curve.multiply(_p, j)
        jp.y = -jp.y
        qj = curve.add(q, jp)

        if qj in l1:
            return (l1[qj] + j * m) % curve.mod

    raise ValueError("Логарифм не найден")