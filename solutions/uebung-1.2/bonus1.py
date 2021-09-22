#!/usr/bin/env python3

"""
Nach dem Satz von Lagrange ist jede natürliche Zahl als Summe von 4 Quadratzahlen darstellbar. Dabei wird 0
auch als Quadratzahl betrachtet.
Schreiben Sie ein Programm, welches vom Benutzer eine natürliche Zahl n anfordert und danach alle Darstellungen der Zahl n
als Summe von 4 Quadraten ausgibt, in welcher die Quadratzahlen nach absteigender Grösse sortiert sind.

Beispiel: Eingabe n = 26; Ausgabe: 9+9+4+4 = 26, 16+9+1+0 = 26, 25+1+0+0 = 26

Zusatz: - Optimieren Sie den Programmcode derart, dass die Laufzeit moeglichst klein ist 
          und so dass Sie möglichst grosse Zahlen in vernünftiger Laufzeit (<= 10 sec) zerlegen können
        - Lesen Sie auf Wikipedia nach, wieviele Darstellungen es gibt und Überpruefen Sie Ihr Programm,
          ob die Anzahl stimmt
"""

from math import sqrt
n = int(input("Welche Zahl soll als Summe von vier Quadratzahlen dargestellt werden? n = "))
a = 0
w=0

m1 = int(sqrt(n))+1
for i in range(m1):
    m2 = int(sqrt(n-i**2))+1
    for j in range(m2):
        m3 = int(sqrt(n-i**2-j**2))+1
        for k in range(m3):
            l = int(sqrt(n-i**2-j**2-k**2))
            w+=1
            if i**2+j**2+k**2+l**2==n and i>=j and j>=k and k>=l:
                print(f"{i**2}+{j**2}+{k**2}+{l**2} = {n}")
                a+=1

print(f"Total: {a} Darstellungen, {w} Prüfungen")