#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bei dieser Prüfungsaufgabe liegt ein funktionierendes Programm vor. Das Programm ist nicht optimal geschrieben, da sich
Code-Teile mehrfach in fast identischer Form wiederholen. Es soll so umgeschrieben werden, dass die
wiederholten Teile in eine neu zu verfassende Funktion ausgelagert werden, welche dann nur mit
verschiedenen Parameterwerten aufgerufen werden braucht.

Analysieren Sie zuerst den Code und versuchen Sie zu verstehen, was er tut.
Lagern Sie dann den wiederholten Teil in eine Funktion aus und rufen Sie die Funktion mit passenden Parameter-Werten auf,
um denselben Output zu erhalten.
"""


def f(listeOrig, kapazitaet):
    """
    Entfernt aus einer Kopie einer Liste solange das jeweils maximale Element, wie die entfernten Elemente in der Summe
    eine bestimmte Zahl (Kapazität) nicht überschreiten. Gibt zudem die originale Liste, 
    die modifizierte Liste, die erreichte Summe, sowie die restliche Kapazität aus.
    
    :param listeOrig: die originale Liste
    :param kapazitaet: die kapazitaet
    """
    liste = listeOrig.copy()
    summe = 0
    maximum = 0

    while len(liste)>0:
        maximum = max(liste)
        if summe + maximum <= kapazitaet:
            liste.remove(maximum)
            summe += maximum
        else: 
            break
    
    print(f"Liste {listeOrig}, verblieben {liste}.\nErreichte Summe: {summe}. Restkapazität: {kapazitaet-summe}\n")


f([10, 13, 15, 3], 40)
f([12, 8, 7, 13, 5, 9, 22, 11], 48)
f([2, 3, 5, 1, 6, 4], 36)
