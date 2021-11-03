#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random as rnd
testdict = {'a' : 5, 'b' : 7, 'c' : 6, 'd': 7, 'e': 4, 'f': 3, 'g': 5, 'h': 3}
testdict['i']=rnd.randint(1,10)
testdict['j']=rnd.randint(1,10)
testdict['k']=rnd.randint(1,10)
"""
Schreiben Sie ein Programm, welches die Zuordnung Schlüssel -> Wert im Wörterbuch testdict umkehrt für alle Werte, 
die nur zu einem Schlüssel gehören. Geben Sie dann das alte und neue Wörterbuch zum Vergleich aus
"""

newdict={}

umkehrbar = []
for k in testdict.keys():
    same = [m for m in testdict.keys() if testdict[m]==testdict[k]]
    if len(same) == 1: 
        umkehrbar.append(k)

# auf 1 Zeile:
# umkehrbar = { k for k in testdict.keys() if len([m for m in testdict.keys() if testdict[m]==testdict[k]]) == 1}

newdict1 = {k : testdict[k] for k in testdict.keys() if k not in umkehrbar}
newdict2 = {testdict[k] : k for k in testdict.keys() if k in umkehrbar}
newdict = {}
newdict.update(newdict1)
newdict.update(newdict2)

print(testdict)
print(newdict)