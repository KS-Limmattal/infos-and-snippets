#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Schreiben Sie eine Klasse namens "Auto" mit folgenden Eigenschaften und Methoden:
    - Eigenschaften: marke     Marke des Autos
                     baujahr   Baujahr des Autos
                     vMax      Maximalgeschwindigkeit in km/h
                     v         aktuelle Geschwindigkeit in km/h
                     
                    
    - Methoden:  __init__         Initialisierung, wobei die aktuelle Geschwindigkeit standardmässig 0 ist
                 __str__          Zeichenketten-Darstellung in der Form wie z.B. 
                                  "Auto von Marke Audi mit Baujahr 2012 und vMax = 220 km/h. Aktuelle Geschwindigkeit v = 70 km/h"
                 beschleunige     erhöhe Geschwindigkeit um 1, sofern Maximalgeschwindigkeit nicht überschritten wird
                 bremse           vermindere Geschwindigkeit um 1, sofern sie dabei nicht negativ wird
                 validiere        überprüfe, ob Baujahr zwischen 1886 und 2022 liegt. 
                                  Wenn nicht, setzte das Baujahr auf 2022 und schreibe eine entsprechende Warnung hin
                                  
Instanzieren Sie dann ein Auto mit Marke Audi mit Baujahr 2012 und vMax = 220 km/h und aktueller Geschwindigkeit 70 km/h,
sowie ein Auto mit Marke Ferrari mit Baujahr 2018 und vMax = 310 km/h und Vorgabewert für die aktuelle Geschwindigkeit.
Validieren Sie die Baujahre der Autos mit Hilfe der "validiere"-Methode und beschleunigen Sie beide Autos 
mit Hilfe der "beschleunige"-Methode und einer for-Schleife um insgesamt 10 km/h.
"""

class Auto:
    def __init__(self, marke, baujahr, vMax, v=0):
        self.marke = marke
        self.baujahr = baujahr
        self.vMax = vMax
        self.v = v
        
    def __str__(self):
        return f"Auto von Marke {self.marke} mit Baujahr {self.baujahr} und vMax = {self.vMax} km/h. Aktuelle Geschwindigkeit v = {self.v} km/h"
    
    def beschleunige(self):
        if self.v <= self.vMax - 1:
            self.v += 1
            
    def bremse(self):
        if self.v >= 1:
            self.v -=1
            
    def validiere(self):
        if (self.baujahr < 1886 or self.baujahr > 2022):
            print(f"Korrigiere Baujahr von {self.baujahr} auf 2022")
            self.baujahr = 2022
            

Audi = Auto("Audi", 2012, 220, 70)
Ferrari = Auto("Ferrari", 2018, 310)

Audi.validiere()
Ferrari.validiere()

for i in range(10):
    Audi.beschleunige()
    Ferrari.beschleunige()
    
