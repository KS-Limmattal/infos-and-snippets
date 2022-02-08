#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Erstelle eine Klasse "Quaternion" zum Rechnen mit Quaternionen mit folgenden Eigenschaften und Methoden:
    - Eigenschaften: r, i, j, k  (für die Komponenten eines Quaternions)
    - Methoden: __str__
                __init__
                __eq__     für Vergleich mit ==
                __add__    Addition von Quaternionen
                __mul__    Multiplikation von Quaternionen
                conjugate  Konjugiertes eines Quaternions
                norm       Norm eines Quaternions
                inv        Inverses eines Quaternions
                 
Erstelle dann die Quaternionen a = -1 + i - 2j + 3k und b = 1 - 2i + 3j - k
und überprüfe mit ihnen die Funktionalität deines Codes
Beispiel: print(f"{a} + {b} = {a+b}")

Zusatz 1: Verbessere die Funktion __str__ so, dass die Ausgabe vereinfacht erfolgt, wie z.B. c = 3+i-k
Zusatz 2: Erstelle eine Klasse Punkt3d mit folgenden Eigenschaften und Methoden:
    - Eigenschaften: x, y, z
    - Methoden: __init__
                __str__
                dist       Distanz zu einem vorgegebenen Punkt
                rotate     Rotation um eine bestimmte Achse durch den Koordinatenursprung und einen Punkt3d 
                           und einen bestimmten Winkel. Realisiere dies durch Konjugation p' = q*p*q^(-1)
                           mit dem Quaternion q = cos(winekl/2) + sin(winkel/2) * normalisierte Achse
                                                   Realteil         Vektoranteil  (Komponenten i,j,k)
                           wobei der Punkt mit dem Vektoranteil p eines Quaternions identifiziert wird
"""

def vorz(v):
    """
    Gibt das Vorzeichen (+ oder -) einer Dezimalzahl zurück
    :param v: die Zahl, deren Vorzeichen zurückgegeben werden soll
    :return: das Vorzeichen
    """
    return "+" if v >= 0 else "-"

def numstr(v,u):
    """
    Gibt die korrekte Darstellung für eine Dezimalzahl mit zugehöriger Einheit (1,i,j,k) zurück
    :param v: die Dezimalzahl
    :param u: die Einheit als Zeichenkette
    :return: die korrekte Darstellung als Zeichenkette (z.B. -2.5j)
    """
    if v==0: 
        return "" 
    else: 
        if v==1 or v==-1: return vorz(v)+u   # Bsp: +1, -1, +i, -i etc.
        return vorz(v) + str(abs(v)) + u     # Bsp: +2, -2, +2i, -2i etc.

def entfernePlus(s):
    """
    Entfernt ein führendes Plus in der Darstellung eines Quaternions (z.B. in +1-2i).
    
    :param s: Zeichenkette, welche das Quaternion darstellt und evtl. ein führendes Plus enthält
    :return: Zeichenkette, ohne führendes Plus, bzw. "0", falls s leer ist.
    """
    
    if len(s)==0: return "0"
    elif s[0]=="+":                 
        return s.replace("+","",1)           # Bsp: +1-2i -> 1-2i
    return s

class Quaternion:
    """
    Eine Klasse zum Rechnen mit Quaternionen. 
    """
    def __init__(self,r,i,j,k):
        self.r=r
        self.i=i
        self.j=j
        self.k=k
    
    def __str__(self):
        return entfernePlus(f"{numstr(self.r,'1')}{numstr(self.i,'i')}{numstr(self.j,'j')}{numstr(self.k,'k')}")
    
    def __eq__(self,q):
        return (self.r==q.r and self.i==q.i and self.j==q.j and self.k==q.k)
    
    def __add__(self,q):
        return Quaternion(self.r+q.r,self.i+q.i,self.j+q.j,self.k+q.k)
    
    def __mul__(self,q):
        x = self.r*q.r - self.i*q.i - self.j*q.j - self.k*q.k
        y = self.r*q.i + self.i*q.r + self.j*q.k - self.k*q.j
        z = self.r*q.j + self.j*q.r + self.k*q.i - self.i*q.k
        w = self.r*q.k + self.k*q.r + self.i*q.j - self.j*q.i
        return Quaternion(x,y,z,w)
    
    def conjugate(self):
        return Quaternion(self.r,-self.i,-self.j,-self.k)
    
    def norm(self):
        return (self*self.conjugate()).r
    
    def inv(self):
        return self.conjugate()*Quaternion(1/self.norm(),0,0,0)
        
a = Quaternion(-1,1,-2,3)
b = Quaternion(1,-2,3,1)
print(f"{a} + {b} = {a+b}")
print(f"({a}) * ({b}) = {a*b}")
print(a.norm())


import math as m

class Point3d:
    """
    Eine Klasse zum Rechnen mit Punkten im 3-dimensionalen Raum
    """
    
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        
    def __str__(self):
        return f"({self.x},{self.y},{self.z})"
   
    def dist(self,q):
        return m.hypot(self.x-q.x, self.y-q.y, self.z-q.z)
    
    def rotate(self,axis,angle):
        c = m.cos(angle/2)
        s = m.sin(angle/2)
        d = axis.dist(Point3d(0,0,0))  # Länge der Achse 
        q = Quaternion(c,axis.x/d*s, axis.y/d*s,axis.z/d*s)
        p = Quaternion(0,self.x,self.y,self.z)
        n=q*p*q.inv()
        return Point3d(n.i,n.j,n.k), q
        
axis = Point3d(1,1,1)
angle = 2*m.pi/3
p = Point3d(3,2,5)
pRot,q = p.rotate(axis,angle)
print(pRot,q)
