# Ganzzahl-Arithmetik

a = 5
b = 11
c = 14

x = a*b+c       # Produkt und Summe
y = a**x        # Potenz

z = b // a      # Ganzzahl-Division (11 // 5 = 2)
z = b % a       # Rest bei Ganzzahl Division (11 % 5 = 1)


# Fliesskommazahlen-Arithmetik

e = 2.3
f = 9.8

r = e/f         # Gewöhnliche Division


# Für kompliziertere Berechnungen braucht es das "math" Modul

import math as m                  
s = m.sqrt(e) - m.cos(m.pi/2)     # elementare Funktionen und Konstanten
t = m.floor(e) + m.ceil(f)        # abrunden bzw. aufrunden
u = m.hypot(e,f)                  # m.sqrt(e**2+f**2), funktioniert auch mit mehr als 2 Argumenten und vermeidet Überlauf bei grossen Argumenten


## Zum Rechnen mit komplexen Zahlen braucht es das "cmath" Modul; Die Zahl i wird dabei durch 1j repräsentiert

import cmath as cm
c1 = 1+1j
c2 = 2-3j

c4 = c1**2-c2
c5 = cm.polar(c1)                 # Darstellung in Polarform als (r,phi)
r = abs(c4)                       # Direkte Berechnung des Betrags 
phi = cm.phase(c4)                # Direkte Berechnung des Winkels

c6 = cm.rect(r, phi)              # Darstellung in Form a+b*j
x = c6.real                       # Realteil
y = c6.imag                       # Imaginärteil


## Für das Rechnen mit Matrizen empfiehlt isch die Verwendung des "numpy" Moduls

import numpy as np
m1 = np.array([[1, 2, 3, 4], [5, 6, -2, 3], [1, 1, 1, 1]])        # Eine 3x4 Matrix, spezifiziert durch die Zeilen
m2 = m1.T                                                         # Transponierte

m3=m1@m2                                                          # Matrix-Produkt (m1*m2 liefert komponentenweise Produkt)
m4=np.linalg.matrix_power(m3,5)                                   # Matrix-Potenz
m5=2*m3+3*m4                                                      # Addition und Multiplikation mit Skalar

s=m5[2,0]                                                         # Matrix-Koeffizient der 3. Zeile und 1. Spalte
m6=m5[1:3,1:3]                                                    # Matrix gebildet aus Zeilen 1-2 und Spalten
                                                                  # Nummerierung beginnt bei 0
form=m6.shape                                                     # Form der Matrix m6, hier (3,4)
m7=np.zeros(form)                                                 # 0-Matrix von der gleichen Form wie m6

d = np.linalg.det(m5)                                             # Determinante
i = np.linalg.inv(m5)                                             # Inverse
ew = np.linalg.eigvals(m5)                                        # Eigenwerte
ew, ev = np.linalg.eig(m5)                                        # Eigenwerte und zugehörige Eigenvektoren

v1 = np.array([1,0,-2])                                           # Vektor
v2 = np.array([2,1,1])
s = v1@v2                                                         # Skalarprodukt von Vektoren
v3 = m2@v2                                                        # Matrix mal Vektor

A = np.array([[1,0,-1],[2,1,3],[4,1,5]])                         
v = np.array([1,-2,3])
x = np.linalg.solve(A,v)                                          # Löse lineares Gleichungssystem A*x = v (mit A invertierbar)
print(np.all(A@x==v))                                             # Überprüfe, ob alle Komponenten von A*x mit denjenigen von v übereinstimmen