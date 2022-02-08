#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Erstelle eine Klasse "Kreis" mit folgenden Eigenschaften und Methoden:
    - Eigenschaften: radius, zentrumX, zentrumY 
    - Methoden: __init__   wobei das Kreiszentrum standardgemäss der Koordinatenursprung ist 
                __str__    mit Ausgabe wie "Kreis mit Zentrum (2.3, 1.45) und Radius 4.42", 
                verschiebe         -> zum Verschieben des Kreises um den Vektor mit Komponenten dx, dy
                skaliereZentrisch  -> um den Kreis am Kreiszentrum mit einem gegebenen Faktor >0 zu skalieren
                enthaeltPunkt      -> um zu Testen, ob ein gegebener Punkt (x,y) auf dem Kreis liegt
                
Instanziere dann ein Objekt dieser Klasse mit Radius 5 und Standard Zentrum,
verschiebe es um den Vektor eine Einheit nach links und 5 Einheiten nach oben,
skaliere es um den Faktor 2
gib ihn mit print aus
und teste für die Punkte (-2, 8) und (7, 11), ob sie auf dem Kreis liegen
"""

class Kreis:
    def __init__(self, radius, zentrumX=0, zentrumY=0):
        self.radius = radius
        self.zentrumX = zentrumX
        self.zentrumY = zentrumY
        
    def __str__(self):
        return f"Kreis mit Zentrum ({self.zentrumX}, {self.zentrumY}) und Radius {self.radius}"
        
    def verschiebe(self, dx, dy):
        self.zentrumX += dx
        self.zentrumY += dy
        
    def skaliereZentrisch(self, faktor):
        self.radius *= faktor
        
    def enthaeltPunkt(self, x, y):
        return (self.zentrumX - x)**2 + (self.zentrumY - y)**2 == self.radius**2
    
kreis = Kreis(5)
kreis.verschiebe(-1,5)
kreis.skaliereZentrisch(2)
print(kreis)
print(f"Enthält der Kreis den Punkt (-2, 8)? -> {kreis.enthaeltPunkt(-2, 8)}")
print(f"Enthält der Kreis den Punkt (7, 11)? -> {kreis.enthaeltPunkt(7, 11)}")