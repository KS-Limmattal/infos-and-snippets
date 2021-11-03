#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random as rnd
testdict = {'a': [1,2,4,7,2], 'b': [2,5,2,3,9,8,23,11], 'c': [2,5,8,2,11,24,23,191], 'd': [24,23,11,13]}
testdict['e'] = [rnd.randint(1,100) for i in range(10)]
"""
Erstelle ein Wörterbuch, welches aus testdict ein Wörterbuch newdict erstellt, welches aus testdict durch
Streichung aller ungeraden Zahlen hervorgeht. Das Programm soll ausserdem zuerst testdict und dann newdict ausgeben,
so dass das Ergebnis manuell verifiziert werden kann. 
"""
newdict = {k : [i for i in testdict[k] if i%2==0] for k in testdict.keys()}
print(testdict)
print(newdict)