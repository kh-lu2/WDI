import random

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, rhs):
        return self.x == rhs.x and self.y == rhs.y
    
    def __hash__(self):
        return hash((self.x, self.y))

    @staticmethod
    def rand_P(lower = -5, upper = 5):
        return Point(*(random.randint(lower, upper) for _ in range(2)))
    
    @staticmethod
    def can_form_sq(A, B):
        return B.x - A.x == B.y - A.y
    
    @staticmethod
    def exists_sq(A, B, data):
        return Point(A.x, B.y) in data and Point(B.x, A.y) in data

    @staticmethod
    def is_in_sq(point, A, B):
        minx, maxx, miny, maxy = min(A.x, B.x), max(A.x, B.x), min(A.y, B.y), max(A.y, B.y)
        return point.x >= minx and point.x <= maxx and point.y >= miny and point.y <= maxy

    @staticmethod
    def empty_sq(A, B, data):
        sum = 0
        for point in data:
            if point == A or point == B:
                continue
            if Point.is_in_sq(point, A, B):
                sum = sum + 1
        return sum == 2

data_size = 10
data = list({Point.rand_P() for _ in range(data_size)})
data_size = len(data)

# tu istnieje 
# data = [Point(0, 0), Point(1, 1), Point(-4, 8), Point(-2, -5), Point(0, -5), Point(0, -3), Point(-2, -3)]

# tu nie istnieje
# data = [Point(0, 0), Point(1, 1), Point(-2, -4), Point(-2, -5), Point(0, -5), Point(0, -3), Point(-2, -3)]

print(*data)
data_size = len(data)
found = 0

for a in data:
    for b in data:
        if a == b:
            continue
        if not Point.can_form_sq(a, b):
            continue
        if not Point.exists_sq(a, b, data):
            continue
        if not Point.empty_sq(a, b, data):
            continue
    
        found = 1

print(f"{"Istnieje" if found else "Nie istnieje"} kwadrat spelniajacy warunki zadania")