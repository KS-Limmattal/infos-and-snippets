#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ersetze in den folgenden Funktionen den behelfsmässigen 'pass' Befehl mit den passenden Anweisungen.
"""

def erstesR(li):
    """Liefert den ersten Listeneintrag zurück, der ein gross- oder kleingeschriebenes 'R' enthält.
    
    :param li: eine Liste bestehend aus Zeichenketten
    :return: der erste Listeintrag mit einem 'R', bzw. eine leere Zeichenkette, falls kein Listeintrag ein 'R' enthält
    """
    
    for l in li:
        if 'r' in l.lower(): return l
        
    return ""
    
def letzteVerdopplung(li):
    """Liefert den letzten Listeneintrag zurück, der einen verdoppelten Buchstaben (wie in 'doppelt', aber nicht
    wie in 'Papa' oder 'Aare') enthält. Belässt die gegebene Liste unverändert.
    
    :param li: eine Liste bestehend aus Zeichenketten
    :return: der letzte Listeneintrag mit verdoppeltem Buchstaben bzw. eine leere Zeichenkette, falls kein Listeintrag
             einen verdoppelten Buchstaben enthält
    """
    
    revLi = li.copy()
    revLi.reverse()  # originale Liste bleibt unverändert
    for l in revLi:
        for i in range(len(l)-1):
            if l[i]==l[i+1]:
                return l
    return ""

def streicheVerdoppelte(li):
    """Streiche aus der gegebenen Liste alle Einträge, die einen verdoppelten Buchstaben (wie in 'doppelt', aber nicht
    wie in 'Papa' oder 'Aare') enthalten. Die gegebene Liste soll verändert werden. Es wird keine Rückgabe erwartet.
    
    :param li: eine Liste bestehend aus Zeichenketten
    """
    
    for l in li:
        for i in range(len(l)-1):
            if l[i]==l[i+1]:
                li.remove(l)
                break
                             
def palindrome(li):
    """Liefert die Liste aller Palindrome (wie in 'Ada', 'Anna' und 'Rentner') zurück, die in einer vorgegebenen Liste vorkommen. 
       Gross-/Kleinschreibung spielt keine Rolle.
    
    :param li: eine Liste bestehend aus Zeichenketten
    :return: eine Liste bestehend aus allen Palindromen der gegebenen Liste, in derselben Reihenfolge wie in dieser Liste
    """
    
    ret = []
    for l in li:
        lLow = l.lower()
        if lLow==lLow[::-1]:
            ret.append(l)
    return ret
    
def schnittbuch(dict1, dict2):
    """Liefert das Wörterbuch zurück, welcher aus allen gemeinsamen Schlüsseln von dict1 und dict2 besteht, welche durch 
       dict1 und dict2 den gleichen Wert zugewiesen erhalten
       
    :param dict1: das erste Wörterbuch
    :param dict2: das zweite Wörterbuch
    :return: das zu konstruierende Durdchschnittsbuch
    """
    
    return {k:v for k,v in dict1.items() if k in dict2.keys() and dict2[k]==v}

def teilbuch(buch, li):
    """Liefert das Teil-Wörterbuch zurück, welcher aus allen Schlüsseln besteht, welche auch in einer gegbenen Liste vorkommen
       
    :param buch: das Wörterbuch
    :param li: die Liste
    :return: das zu konstruierende Teilbuch
    """
    
    return  { k:v for k,v in buch.items() if k in li}
