import math
import numpy as np
from pydantic import BaseModel

class Vector3(BaseModel):
    """Class for doing spatial calculations in 3 dimensions"""
    x: float
    y: float
    z: float

    def __init__(__pydantic_self__, x: float, y: float, z: float):
        super().__init__(x=x, y=y, z=z)

    def as_tuple(self):
        return (self.x, self.y, self.z)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __add__(self, o: object):
        return Vector3(self.x + o.x, self.y + o.y, self.z + o.z)

    def __mull__(self, o: object):
        return Vector3(self.x * o.x, self.y * o.y, self.z * o.Z)

    def __sub__(self, o: object):
        return Vector3(self.x - o.x, self.y - o.y, self.z - o.z)

    def __truediv__(self, o: object):
        return Vector3(self.x / o.x, self.y / o.y, self.z / o.z)

    def __floordiv__(self, o: object):
        return Vector3(self.x // o.x, self.y // o.y, self.z // o.z)

    def __eq__(self, o: object):
        if o == None:
            return False
        return self.x == o.x and self.y == o.y and self.z == o.z

    def eucl_distance_to(self, p2):
        return math.sqrt(
            (p2.x - self.x) ** 2 +
            (p2.y - self.y) ** 2 +
            (p2.z - self.z) ** 2
        )

    def distance_to(self, p2):
        return (self.x - p2.x, self.y - p2.y, self.z - p2.z)

    def as_numpy(self):
        return np.array([
            self.x,
            self.y,
            self.z
        ])

class Vector2(BaseModel):
    """Class for doing spatial calculations in 2 dimensions"""
    x: float
    y: float

    def __init__(__pydantic_self__, x: float, y: float):
        super().__init__(x=x, y=y)

    def as_tuple(self):
        return (self.x, self.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __add__(self, o: object):
        return Vector2(self.x + o.x, self.y + o.y)

    def __mull__(self, o: object):
        return Vector2(self.x * o.x, self.y * o.y)

    def __sub__(self, o: object):
        return Vector2(self.x - o.x, self.y - o.y)

    def __truediv__(self, o: object):
        return Vector2(self.x / o.x, self.y / o.y)

    def __floordiv__(self, o: object):
        return Vector2(self.x // o.x, self.y // o.y)

    def __eq__(self, o: object):
        if o == None:
            return False
        return self.x == o.x and self.y == o.y

    def eucl_distance_to(self, p2):
        return math.sqrt((p2.x - self.x) ** 2 + (p2.y - self.y) ** 2)

    def distance_to(self, p2):
        return Vector2(self.x - p2.x, self.y - p2.y)

    def as_vector3(self):
        return Vector3(self.x, self.y, 0)

    def as_numpy(self):
        return np.array([
            self.x,
            self.y
        ])

class Plane2(BaseModel):
    """Class for doing spatial calculations with a 2d plane"""
    lt: Vector2
    lb: Vector2
    rt: Vector2
    rb: Vector2

    def __init__(__pydantic_self__, lt: Vector2, lb: Vector2, rt: Vector2, rb: Vector2):
        super().__init__(lt=lt, lb=lb, rt=rt, rb=rb)

    @property
    def wt(self):
        return self.rt.x - self.lt.x

    @property
    def wb(self):
        return self.rb.x - self.lb.x
    
    @property
    def hl(self):
        return self.lb.y - self.lt.y

    @property
    def hr(self):
        return self.rb.y - self.rt.y

    @property
    def avg_h(self):
        return (self.hr + self.hl) / 2

    @property
    def avg_w(self):
        return (self.wb + self.wt) / 2

    @classmethod
    def from_list(cls, l):
        lt = Vector2(**l[0])
        lb = Vector2(**l[1])
        rt = Vector2(**l[2])
        rb = Vector2(**l[3])
        
        return cls(lt, lb, rt, rb)

    def get_transform_plane(self, plane2):
        return Plane2(
            self.lt.distance_to(plane2.lt),
            self.lb.distance_to(plane2.lb),
            self.rt.distance_to(plane2.rt),
            self.rb.distance_to(plane2.rb),
        )

    def transform(self, t):
        self.lt += t.lt
        self.lb += t.lb
        self.rt += t.rt
        self.rb += t.rb

    def as_numpy(self):
        return np.array([
            self.lt.as_tuple(),
            self.lb.as_tuple(),
            self.rt.as_tuple(),
            self.rb.as_tuple(),
            ])

    def as_list(self):
        return [
            self.lt.as_tuple(),
            self.lb.as_tuple(),
            self.rt.as_tuple(),
            self.rb.as_tuple(),
        ]

    def __eq__(self, o: object):
        if o == None:
            return False
        return self.lt == o.lt and self.lb == o.lb and self.rt == o.rt and self.rb == o.rb
