#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Schreiben Sie ohne Verwendung des numpy-Moduls eine Klasse namens "Mat2" für reelle 2x2-Matrizen 
mit folgenden Eigenschaften und Methoden:
    - Eigenschaften: x11, x12, x21, x22 (Komponenten der Matrix)
    - Methoden: __init__          mit Standardwerten entsprechend der Einheitsmatrix
                __str__           Darstellung als Zeichenkette auf 2 Zeilen wie z.B. 
                                    [1.5  2.3] 
                                    [3.1  4.0]
                __add__           Matrizenaddition
                __sub__           Matrizensubtraktion
                __mul__           Matrizenmultiplikation
                det               Determinante
                invertierbar      liefert zurück, ob die Matrix invertierbar ist
                
Instanzieren Sie dann zwei Matrizen A und B, wovon A die Zeilen [1, 2] und [3, 4] und B die Zeilen [2, -1], [3, 1.5] hat.
Geben Sie dann mit Hilfe des print-Befehls das Matrizenprodukt (A+B)*(A-B) aus. 
"""

class Mat2:
    def __init__(self, x11=1, x12=0, x21=0, x22=1):
        self.x11 = x11
        self.x12 = x12
        self.x21 = x21
        self.x22 = x22
        
    def __str__(self):
        return f"[{self.x11}  {self.x12}]\n[{self.x21}  {self.x22}]"
    
    def __add__(self, other):
        return Mat2(self.x11+other.x11, self.x12+other.x12, self.x21+other.x21, self.x22+other.x22)
    
    def __sub__(self, other):
        return Mat2(self.x11-other.x11, self.x12-other.x12, self.x21-other.x21, self.x22-other.x22)

    def __mul__(self,other):
        z11 = self.x11*other.x11 + self.x12*other.x21
        z12 = self.x11*other.x12 + self.x12*other.x22
        z21 = self.x21*other.x11 + self.x22*other.x21
        z22 = self.x21*other.x12 + self.x22*other.x22
        return Mat2(z11,z12,z21,z22)
    
    def det(self):
        return self.x11*self.x22 - self.x21*self.x12
    
    def invertierbar(self):
        return self.det() != 0
    
    
A = Mat2(1,2,3,4)
B = Mat2(2,-1,3,1.5)
C = (A+B)*(A-B)
print(f"Produkt (A+B)*(A-B) = \n{C}")
