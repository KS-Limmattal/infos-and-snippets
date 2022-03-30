#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Klasse "Pacman", Oberklasse von "Figur" mit zusätzlichen

- Eigenschaften: lifes       (verbliebene Leben)
                 score       (Punktezahl)
                 canEatGhost (ob Pacman gerade eine Kraftpille Intus hat)

- Methoden:      decLives (vermindert Lebenszahl, falls > 0; schreibe "Game over" andernfalls)
                 incScore (nimmt eine Zeichenkette s als Argument und erhöht die Punktezahl um
                           10 Punkte, falls s == "Punkt"
                           100 Punkte, falls s == "Frucht"
                           200 Punkte, falls s == "Kraftpille"
"""

import Figur

score_dict = {"Punkt": 10, "Frucht": 100, "Kraftpille": 200}

class Pacman(Figur):
    def __init__(self, lifes=3, score=0, canEatGhost=True):
        self.lifes = lifes
        self.score = score
        self.canEatGhost = canEatGhost
        
    def decLives(self):
        if self.lifes > 0:
            self.lifes -=1
        else:
            print("Game over")
    
    def incScore(s, self):
        self.score += score_dict[s]
