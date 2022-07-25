from typing import Callable
from math import sqrt
from itertools import count

def integrate(
    f: Callable[[float], float],
    start: float,
    end: float,
    d: float = 0.0001
) -> float:
    """
    Calculate the area under a function between an interval using the
    average of the left and right Riemann sum.
    """
    rectangles = int((end - start) / d)
    area = 0.0
    for i in range(rectangles):
        area += f(start + d * i) * d
        area += f(start + d * (i + 1)) * d
    area /= 2
    return area

def corner(x: float) -> float:
    """
    A function that translates the bottom half of a circle to the first
    quadrant.
    """
    return -sqrt(1 - (x - 1) ** 2) + 1

def line(a: float, x: float) -> float:
    """
    A linear, well, line.
    """
    return a * x

total = integrate(corner, 0, 1)

for n in count(1):
    slope = 1 / n
    # The intersecting area under two curves is the minimum of the two curves
    # at any point.
    intersecting = integrate(
        lambda x: min(corner(x), line(slope, x)),
        0,
        1
    )
    percent = intersecting / total * 100
    if percent < 0.1:
        print(n)
        break
