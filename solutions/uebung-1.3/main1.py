#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Schreiben Sie ein Programm mit 
Eingabe: eine komplexe Zahl c (in der Form a+bj)
Ausgabe: Benachrichtigung darüber, ob c zur Mandelbrot-Menge gehört.

Die Mandelbrot-Menge besteht aus allen komplexen Zahlen c, für welche die Folge z_0; z_1; z_2; ...
definiert durch z_0 = 0; z_(n+1) = z_n^2 + c beschränkt ist.

Für Unbeschränktheit dieser Folge genügt dabei, dass ein Folgenglied betragsmässig > 2 ist.
Da nicht unendlich viele Folgenglieder berechnet werden können, werden in der Praxis nur 
eine feste Anzahl (z.B. 100) Folgelieder betrachtet.

Zusatz: Visualisiere die Mandelbrot-Menge 
(z.B. mit Hilfe des mathplotlib-Moduls via pyplot.imshow(T), 
 wobei T ein numpy-array ist, welches die Zugehörigkeit zur Mandelbrot-Menge 
 im Rechteck mit -2<= Re(c) <= 1, -1 <= Im(c) <=1 codiert)
"""

from cmath import *
c = complex(input("Geben Sie eine komplexe Zahl in der Form a+bj ein! c = "))

N = 100 
z = 0
enthalten = True

for i in range(N):
    z = z**2 + c
    if abs(z) > 2:
        enthalten = False
        break

wort = "" if enthalten else "nicht "
print(f"Die Zahl {c} ist {wort}in der Mandelbrotmenge enthalten")