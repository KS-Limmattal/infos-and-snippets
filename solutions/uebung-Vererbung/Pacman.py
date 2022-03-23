#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Klasse "Pacman", Oberklasse von "Figur" mit zusätzlichen

- Eigenschaften: lives       (verbliebene Leben)
                 score       (Punktezahl)
                 canEatGhost (ob Pacman gerade eine Kraftpille Intus hat)

- Methoden:      decLives (vermindert Lebenszahl, falls > 0; schreibe "Game over" andernfalls)
                 incScore (nimmt eine Zeichenkette s als Argument und erhöht die Punktezahl um
                           10 Punkte, falls s == "Punkt"
                           100 Punkte, falls s == "Frucht"
                           200 Punkte, falls s == "Kraftpille"
"""

