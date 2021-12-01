#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prüfungsaufgabe 1 (vom 24.11.2021)

Berechnen Sie mittels eines Programms die Wahrscheinlichkeit, dass bei einem 
Vierfach-Wurf von Würfeln eine dreifache, aber keine vierfache Augenzahl auftritt. 
Generieren Sie dazu alle günstigen Quadrupel von Augenzahlen.
Geben Sie die Wahrscheinlichkeit als Bruch und Prozentzahl mit 2 Nachkommastellen 
in einem sauber formatierten Satz aus.
"""

guenstig = 0
total = 0
for i in range(1,7):
    for j in range(1,7):
        for k in range(1,7):
            for l in range(1,7):
                total+=1
                if (i==j==k!=l) or (j==k==l!=i) or (k==l==i!=j) or (l==i==j!=k):
                    guenstig+=1

print(f"Die W'keit für eine dreifache, aber keine vierfache Augenzahl beträgt {guenstig}/{total} = {100*guenstig/total:.2f} %")