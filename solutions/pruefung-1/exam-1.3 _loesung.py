#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prüfungsaufgabe 3 (vom 24.11.2021)

Fordern Sie den Benutzer zur Eingabe einer natürlichen Zahl auf. Bilden Sie dann die Zahlenfolge, welche
mit der eingegebenen Zahl beginnt und in jedem Schritt 
- die Zahl durch 2 teilt, falls sie gerade ist, bzw. 
- die Zahl mit 3 multipliziert und danach 1 dazu-addiert, falls sie ungerade ist

Wenn die Zahl 1 erreicht wird, hören Sie auf. 

Fügen Sie diese Folgenglieder in eine Liste ein. Geben Sie die Anzahl Schritte bis zur Erreichung der 1 aus, 
sowie die Liste der Folgenglieder, die bis dahin berechnet worden sind.

Beispiel: 
    Eingabe: 17, 
    Ausgabe: "Es sind 12 Schritte, bis die 1 erreicht wird"
             "[17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]"
"""

n = int(input('Geben sie eine natürliche Zahl ein: '))
folge = [n]


while n!=1:
    if n % 2 == 0:
        n = n//2
    else:
        n = 3*n + 1

    folge.append(n)

print(f'Es sind {len(folge)-1} Schritte, bis die 1 erreicht wird')
print(folge)