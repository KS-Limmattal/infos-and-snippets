#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Klasse "Figur" mit 

- Eigenschaften: x, y, (für Position) 
                 dir   (Richtung: "Up", "Down", "Left" oder "Right")
                 playground (numpy array bestehend aus Nullen (frei) und Einsen (Wand))
                
- Methoden:  __init__
             canMove (überprüft, ob sich Figur in gegebener Richtung bewegen kann)
             Bsp: Ist self.x == 4, self.y == 7, self.dir = "Up" und self.playground[4][6] == 0, 
                  so muss der Rückgabewert True sein
"""

dir_dict = {"Up": (0,-1), "Down": (0,1), "Left": (-1,0), "Right": (1,0)}

class Figur:
    def __init__(self, x, y, dir, playground):
        self.x = x
        self.y = y
        self. dir = dir
        self. playground = playground
    
    def canMove(self):
        dx, dy = dir_dict[dir]
        newX = self.x + dx
        newY = self.y + dy
        maxX, maxY = self.playground.shape
        return newX >= 0 and newX <= maxX and newY >= 0 and newY <=maxY and self.playground[newX][newY] != 1
        