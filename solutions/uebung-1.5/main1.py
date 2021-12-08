#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ersetze in den folgenden Funktionen den behelfsmässigen 'pass' Befehl mit den passenden Anweisungen.
Rufe danach die definierten Funktionen auf und gib damit folgendes in einem nett formattierten Satz aus:
    - die Anzahl der Paare von 10 Punkten der Ebene
    - die Anzahl Matrix-Elemente auf oder oberhalb der Diagonalen für eine 20x20 Matrix
    - die Summe aller Beträge der Eigenwerte der 2x2-Matrix [[e,pi],[e+pi,e*pi]]
    - die Summe aller Beträge der Eigenwerte der 4x4-Matrix mit a_{r,s} = r**2*s+s für 1<=r,s<=4
    - eine Approximation der Wurzel der Zahl 10 auf 4 Nachkommastellen genau
    - eine Approximation der Wurzel der Zahl 2 auf 8 Nachkommastellen genau
    - die Summe aller Beträge der Eigenwerte der Matrix [[w2,w3],[w5, w6]], wobei w2, w3, w5 und w6 für 
      Approximationen der Wurzeln der entsprechenden Zahl (2,3,5 bzw. 6) auf 4 Nachkommastellen sind
"""

def anzahlPaare(n):  
    """
    Gibt die Anzahl Paare bei vorgegebener Anzahl Objekte zurück
    
    :param n: Anzahl Objekte
    :return: Anzahl möglicher Paare
    """
    return n*(n-1)//2

import numpy as np
def summeAbsEigval(A):
    """
    Gibt die Summe aller Beträge der Eigenwerte (mit Vielfachheiten) der gegebenen Matrix zurück
    
    :param A: Die gegebene Matrix
    :return: Die Summe aller Eigenwert-Beträge
    """
    eig, val = np.linalg.eig(A)
    return np.sum(abs(eig))
    

def wurzelApprox(x, eps):
    """
    Gibt eine Approximation an den Wert der Wurzel einer Zahl zurück, die nicht weiter als eine bestimmte Toleranz
    vom wahren Wert entfernt ist. Verwende dazu das Heron-Verfahren. Die sqrt-Funktion darf nicht eingesetzt werden
    
    :param x:   die Zahl, deren Wurzel zu berechnen ist
    :param eps: die vorgegebene Toleranz
    :return: der Näherungswert an die Wurzel der gegebenen Zahl
    """
    r = x/2
    while (abs(r - x/r) >= eps): # Bemerkung: die wahre Wurzel von x liegt zwischen r und x/r
        r = (r+x/r)/2
        
    return r


print(f"Die Anzahl Paare von 10 Punkten der Ebene beträgt {anzahlPaare(10)}.")
print(f"Die Anzahl Matrix-Elemente auf oder oberhalb der Diagonalen beträgt für eine 20x20 Matrix {anzahlPaare(20)+20} \n")

import math as m
A = [[m.e, m.pi],[m.e+m.pi, m.e*m.pi]]
print(f"Die Summe aller Beträge der Eigenwerte der Matrix \n {A} \n ist {summeAbsEigval(A)} \n")

B=np.zeros((4,4),dtype=float)
for r in range(1,5):
    for s in range(1,5):
        B[r-1,s-1]=r**2*s+s
print(f"Die Summe aller Beträge der Eigenwerte der Matrix \n {B} \n ist {summeAbsEigval(B)} \n")

print(f"Die Wurzel von 10 ist auf 4 Nachkommastellen genau {wurzelApprox(10,10**-4):.4f}")

print(f"Die Wurzel von 2 ist auf 8 Nachkommastellen genau {wurzelApprox(2,10**-8):.8f} \n")

eps=10**-4
C=np.array([[wurzelApprox(2,eps), wurzelApprox(3,eps)],[wurzelApprox(5,eps), wurzelApprox(6,eps)]])
print(f"Die Summe aller Beträge der Eigenwerte der Matrix \n {C} \n ist {summeAbsEigval(C)}")
