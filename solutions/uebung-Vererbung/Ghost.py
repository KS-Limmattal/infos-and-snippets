#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Klasse "Ghost", Oberklasse von "Figur" mit zusätzlichen

- Eigenschaften: mustGoHome       (True oder False)
                 isInCage         (True oder False)       

- Methoden:      chooseDir (gibt eine zufällige Richtung "Up", "Down", "Left" oder "Right" zurück)
                 computeSteps (berechnet Anzahl Schritte, welche der Geist zur als Argumente übergebenen
                               Position auf leerem Spielfeld zurücklegen muss)
"""

import Figur
from random import choice

class Ghost(Figur):
    def __init__(self, mustGoHome=False, isInCage=True):
        super().__init__()
        self.mustGoHome = mustGoHome
        self.isInCage = isInCage
        
    def chooseDir(self):
        return choice(["Up", "Down", "Left", "Right"])

    def computeSteps(self, x, y):
        return abs(self.x-x) + abs(self.y-y)
