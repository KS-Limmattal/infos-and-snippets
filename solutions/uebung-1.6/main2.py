#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Erstelle eine Klasse namens "Vektor3d" mit folgenden Eigenschaften und Methoden:
    - Eigenschften: x,y,z
    - Methoden: __init__
               __str__       mit Ausgabe wie "Vektor (1, 5, -3)"
               __add__       Vektoraddition
               __sub__       Vektorsubtraktion
               __neg__       Gegenvektor
               __truediv__   Division durch einen Skalar
              __rmul__       Multiplikation mit einem Skalar (von links)
              __mul__        Skalarprodukt mit einem anderen Vektor
              betrag         Betrag des Vektors
              normalisiert   der normalisierte Vektor
              vektorProd     Vektorprodukt mit einem anderen Vektor

Instanziere dann einen Vektor v mit Komponenten 1, 2, 3, einen Vektor w mit Koordinaten 4, 2, -1 
und definiere einen Skalar s = 4
Überprüfe dann die Funktionalität deines Codes, indem du die Methoden auf die Vektoren v, w und den Skalar s anwendest
Beispiel: print(f"{v} + {w} = {v+w}")
"""
from math import hypot 

class Vektor3d:
    """
    Eine Klasse zum Rechnen mit 3d-Vektoren
    """
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self):
        return f"Vektor ({self.x}, {self.y}, {self.z})"
        
    def __add__(self,w):
        return Vektor3d(self.x+w.x, self.y+w.y, self.z+w.z)

    def __sub__(self,w):
        return Vektor3d(self.x-w.x, self.y-w.y, self.z-w.z)
    
    def __neg__(self):
        return Vektor3d(-self.x,-self.y,-self.z)
    
    def __truediv__(self, s):
        return Vektor3d(self.x/s,self.y/s,self.z/s)
    
    def __rmul__(self,t):
        return Vektor3d(self.x*t,self.y*t,self.z*t)
    
    def __mul__(self,w):
        return self.x*w.x+self.y*w.y+self.z*w.z
        
    def betrag(self):
        return hypot(self.x,self.y,self.z)
    
    def normalisiert(self):
        return self / self.betrag()
    
    def vektorProd(self,w):
        return Vektor3d(self.y*w.z-self.z*w.y, self.z*w.x-self.x*w.z, self.x*w.y-self.y*w.x)
    
v = Vektor3d(1,2,3)
w = Vektor3d(4,2,-1)
s = 4

print(f"{v} + {w} = {v+w}")
print(f"{v} - {w} = {v-w}")
print(f"-{v} = {-v}")
print(f"|v| = {v.betrag()}")
print(f"{v} normalisiert: {v.normalisiert()}")
print(f"{v} / {s} = {v/s}")
print(f"{s} * {v} = {s*v}")
print(f"{v} * {w} = {v*w}")
print(f"{v} x {w} = {v.vektorProd(w)}")