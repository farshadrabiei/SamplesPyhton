import collections


def collect():
    Point = collections.namedtuple("Point", "x y")
    p1 = Point(10, 20)
    p2 =Point(30,40)
    print(p1,p2,p1)

    print(p1.x)
    print(p2.y)
