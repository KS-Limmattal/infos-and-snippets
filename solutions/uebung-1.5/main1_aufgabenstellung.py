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
    pass

import numpy as np
def summeAbsEigval(A):
    """
    Gibt die Summe aller Beträge der Eigenwerte (mit Vielfachheiten) der gegebenen Matrix zurück
    
    :param A: Die gegebene Matrix
    :return: Die Summe aller Eigenwert-Beträge
    """
    pass

def wurzelApprox(x, eps):
    """
    Gibt eine Approximation an den Wert der Wurzel einer Zahl zurück, die nicht weiter als eine bestimmte Toleranz
    vom wahren Wert entfernt ist. Verwende dazu das Heron-Verfahren. Die sqrt-Funktion darf nicht eingesetzt werden
    
    :param x:   die Zahl, deren Wurzel zu berechnen ist
    :param eps: die vorgegebene Toleranz
    :return: der Näherungswert an die Wurzel der gegebenen Zahl
    """
    pass

