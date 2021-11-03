#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Schreiben Sie ein Programm mit 
Eingabe: eine komplexe Zahl c (in der Form a+b*j)
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

import numpy as np
import matplotlib.pyplot as plt

X_RES = 801 
Y_RES = 601
MAX_ITER = 100


x = np.linspace(-2,1,X_RES)
y = np.linspace(-1,1,Y_RES)
c = np.array([[a+b*1j for a in x] for b in y])
z = np.zeros(c.shape)+0*1j
# it = np.zeros(c.shape)

for i in range(MAX_ITER):
    T = abs(z)<=2
    z[T]=z[T]**2+c[T]
    # it[T]+=1

plt.imshow(T)    
# plt.imshow(it, cmap=plt.cm.twilight_shifted)