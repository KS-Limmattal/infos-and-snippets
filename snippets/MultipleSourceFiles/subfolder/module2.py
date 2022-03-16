#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""

class Vector3d:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return f"Vektor ({self.x}, {self.y}, {self.z})"
    def __add__(self, other):
        return Vector3d(self.x+other.x, self.y+other.y, self.z+other.z)
    def __sub__(self, other):
        return Vector3d(self.x.other.x, self.y-other.y, self.z-other.z)
    def __rmul__(self, s):
        return Vector3d(s*self.x, s*self.y, s*self.z)
    def to_json(self):
        return {"x": self.x, "y": self.y, "z": self.z}

    
if __name__ == '__main__':   # wird nur ausgeführt, wenn diese Datei als Skript ausgeführt wird
    v = Vector3d(2,4,5)
    w = Vector3d(-2,1,3)
    s = 2
    print(f"{v} + {s}*{w} = {v+s*w}")