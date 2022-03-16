#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import hypot
from subfolder.module2 import Vector3d

class Point3d:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __str__(self):
        return f"Punkt ({self.x}, {self.y}, {self.z})"
    def dist(self,other):
        v = Vector3d(self.x-other.x, self.y-other.y, self.z-other.z)
        return hypot(v.x, v.y, v.z)
    def to_json(self):
        return {"x": self.x, "y": self.y, "z": self.z}

def pointInput(s):
    print(s)
    x = float(input("x = "))
    y = float(input("y = "))
    z = float(input("z = "))
    return Point3d(x,y,z)