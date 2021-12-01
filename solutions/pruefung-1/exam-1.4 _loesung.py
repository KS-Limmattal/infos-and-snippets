#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prüfungsaufgabe 4 (vom 24.11.2021)

Im Folgenden wird das Wörterbuch zufallsbuch vorgegeben, dessen Schlüssel Buchstaben a-m sind und deren Werte
zufällig zugeordnete Tiernamen (aus einer vorgegebenen Liste von Tiernamen) sind

Schreiben Sie ein Programm, welches zu jedem Schlüssel (Buchstaben a-m) des Wörterbuchs, 
welcher im zugeordneten Tiernamen vorkommt, einen Satz wie 
'Der Buchstabe f kommt im Tiernamen Giraffe vor.' hinschreibt.
Dabei ist es egal, ob der Buchstabe im Tiernamen gross- oder kleingeschrieben ist. 
Lassen Sie zudem ihr Programm die Liste aller Buchstaben ausgeben, die nicht im zugeordneten Tiernamen vorkommen.
"""
# VORGEGEBENER TEIL (bitte nicht abändern)
import numpy as np
import random as rnd
li1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
li2 = ['Esel', 'Affe', 'Giraffe', 'Krokodil', 'Löwe', 'Emu', 'Katze', 'Chamäleon', 'Bartgeier']
zufallsbuch = {x:rnd.choice(li2) for x in li1}
print(zufallsbuch)
# ENDE VORGEGEBENER TEIL

# BEGINN DES EIGENTLICHEN PROGRAMMS (bitte ergänzen)
li = []
for x, w in zufallsbuch.items(): 
    if x in w.lower():
        print(f"Der Buchstabe {x} kommt im Tiernamen {w} vor.")
    else:
        li.append(x)

print(f"Die Buchstaben in der Liste {li} kommen nicht im zugeordneten Tiernamen vor")