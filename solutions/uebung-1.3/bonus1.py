#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1) Lassen Sie den Benutzer zwei natürliche Zahlen m und n eingeben
2) Kreieren Sie eine mxn Matrix, deren Einträge 1,2,...,m*n sind (1,...,n in oberster Zeile).
3) Die 1 ist keine Primzahl. Ersetzen Sie diese Zahl durch eine 0 (== keine Primzahl)
3) Führen Sie die Sieb-Methode von Erathostenes durch. Was keine Primzahl ist, soll dabei durch eine 0 ersetzt werden. 
   Schreiben Sie dabei in jedem Schritt hin, wessen Vielfachen gestrichen werden und die Matrix, die dabei entsteht
4) Erzeugen Sie einen Vektor primes, der die Primzahlen von 1 bis m*n enthält und geben Sie ihn aus
"""

import numpy as np
m = int(input("input Anzahl Zeilen: "))
n = int(input("input Anzahl Spalten: "))

v=np.arange(m*n)+1          # Vektor bestehend aus den Zahlen 1 bis m*n

print(f"Sieb des Erathostenes: Startmatrix \n {v.reshape(m,n)}")
v[0]=0
print(f"Streiche die 1: Matrix \n {v.reshape(m,n)}")

for i in range(2,int((m*n)**0.5)+1):
    if v[i-1]!=0:
        print(f"Streiche die Vielfachen der Zahl {i}")
        c=2
        while c*i <= m*n:
            v[i*c-1]=0
            c+=1
        print(f"Entstandene Matrix \n {v.reshape(m,n)}")

primes = v[v!=0]
print(f"Die Primzahlen von 1 bis {m*n} lauten: {primes}")