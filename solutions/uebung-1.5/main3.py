#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bei dieser Übung liegt ein funktionierendes Programm vor. Das Programm ist nicht optimal geschrieben, da sich
Code-Teile mehrfach in fast identischer Form wiederholen. Es soll so umgeschrieben werden, dass die
wiederholenden Teile in zwei neu zu verfassenden Funktionen ausgelagert werden, welche dann nur mit
verschiedenen Parameterwerten aufgerufen werden brauchen.

1) Analysiere zuerst den Code und versuche zu verstehen, was er tut. Dokumentiere dies durch Code-Kommentare.
Lagere dann den wiederholten Teil in eine Funktion aus.

2) Ändere nun das Programm so ab, dass es auch für kubische Funktionen statt für quadratische Funktionen funktioniert.
Implementiere dazu die Funktion 'kubisch' und verwende sie beim Aufruf der Funktion 'schnittpunkte'


Zusatz 1: Welche theoretische Erkenntnis machst du, wenn du die Funktion schnittpunkt(f,x1,x2) 
für quadratische Funktionen f(x) mit verschiedenen Parameterwerten aufrufst? Welche Vereinfachung des Codes wäre 
in diesem Falle möglich?

Zusatz 2: Stelle das gelöste Problem graphisch mit Hilfe des matplotlib-Moduls dar
"""

def quadratisch(x):
    """Berechnet einen Funktionswert einer vorderfinierten quadratischen Funktion an gegebener Stelle

    :param x: Stelle, an welcher die quadratische Funktion ausgewertet werden soll
    :return: Funktionswert
    """
    
    a=1; b=2; c=3 # Beispielsparameter
    return a*x**2+b*x+c

def kubisch(x):
    """Berechnet einen Funktionswert einer vorderfinierten kubischen Funktion an gegebener Stelle

    :param x: Stelle, an welcher die kubische Funktion ausgewertet werden soll
    :return: Funktionswert
    """
    
    a=1; b=2; c=3; d=4 # Beispielsparameter
    return a*x**3+b*x**2+c*x+d

def abl(f,x):
    """Berechnet numerisch die Ableitung einer quadratischen Funktion an gegebener Stelle

    :param f: Funktion, die abgeleitet werden soll
    :param x: Stelle, an welcher die quadratische Funktion ausgewertet werden soll
    :return: Steigung und Funktionswert
    """
    
    eps = 10**-8
    y = f(x)
    z = f(x+eps)
    m = (z-y)/eps
    print(f"Tangentengleichung: y = {m:.2f}*(x-{x:.2f}) + {y:.2f}")
    return m, y

def schnittpunkt(f,x1,x2):
    """Berechnet den Schnittpunkt zweier Tangenten an den Graphen einer Funktion
    
    :param f: Funktion, an deren Graphen Tangenten gelegt werden
    :param x1: x-Koordinate des ersten Punkts des Graphen, bei dem eine Tangente gelegt wird
    :param x2: x-Koordinate des zweiten Punkts des Graphen, bei dem eine Tangente gelegt wird
    :return: die x- und y-Koordinate des Schnittpunkts der Tangenten
    :raises ValueError: falls die Tangenten parallel sind
    """
    
    m1, y1 = abl(f,x1)
    m2, y2 = abl(f,x2)
    if m2!=m1:
        x = (m1*x1-m2*x2+y2-y1)/(m1-m2)    # Lösung der Gleichung m1*(x-x1)+y1 = m2*(x-x2)+y2
        y = m1*(x-x1)+y1
        return x,y
    else:
        raise ValueError("Parallele Tangenten")
        
        
x,y = schnittpunkt(kubisch, 0.3, 2.2)
print(f"Die Koordinaten des Schnittpunkts lauten (x,y) = ({x:.4f}, {y:.4f})")