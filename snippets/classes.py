#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Eine Klasse ist ein Bauplan für Objekte eines bestimmten Typs.
Eine Instanz einer Klasse ist eine Realisierung dieses Bauplans.

Klassen haben 
- Eigenschaften: Variablen, welche alle Instanzen derselben Klasse haben
- Methoden: Funktionen, welche alle Instanzen derselben Klasse haben, und welche eine Zustandsänderung einer Instanz ermöglichen
            Jede Methode der Klasse muss als erstes Argument "self" haben. Mit diesem Wort lässt sich auf die Eigenschaften einer
            Instanz zugreifen. Beim Aufruf muss dieses erste Argument weggelassen werden, da es automatisch übergeben wird

Eine Klasse (Bauplan) muss zuerst definiert werden, bevor Instanzen der Klasse angelegt werden können.
Bei der Instanzierung von Objekten wird die __init__ Methode der Klasse aufgerufen, um die Instanz zu konstruieren.

Der Vorteil von Klassen liegt darin, dass Variablen und Funktionen, die zum selben Typ von Objekt gehören, gebündelt werden können.
"""

class Mensch:
    """
    Diese Klasse realisiert einen Bauplan für einen Menschen
    Die Eigenschaften eines Menschen sollen der Vorname, Nachname, und das Alter (in Jahren) sein
    Die Methoden dieser Klasse sollen die Ausgabe des vollen Namens, eine Funktion zur Änderung des Nachnamens, 
    sowie eine Funktion zur Inkrementierung (=Erhöhung um 1) des Alters sein.
    """
    def __init__(self, vorname, nachname, alter=0):
        """
        Konstruktor (konstruiert einen konkreten Menschen, also eine Instanz der Klasse)
        
        param vorname: der zugewiesene Vorname
        param nachname: der zugewiesene Nachname
        param alter: das zugewiesene Alter (standardmässig 0)
        """
        self.vorname = vorname    
        self.nachname = nachname  
        self.alter = alter        
        
    def name(self):
        """
        return: der komplette Name des Menschen
        """
        return f"{self.vorname} {self.nachname}"
    
    def aendereName(self, nachname):
        self.nachname = nachname

    def inkrementiereAlter(self):
        self.alter+=1


# Instanzierung von Menschen (Objekten der Klasse Mensch) erfolgen nach der Definiton der Klasse

exPraesident = Mensch("Donald", "Trump", 75)
baby = Mensch("Laura", "Müller")

# Nun können diese Instanzen, ihre Eigenschaften und Methoden verwendet werden

print(f"Ein amerikanischer Expräsident heisst {exPraesident.name()}.")
exPraesident.aendereName("Trumpovski")
print(f"Der Expräsident heisst neu {exPraesident.name()}.")
print(f"Aktuell ist das Baby {baby.alter} Jahre alt")
baby.inkrementiereAlter()
print(f"Nun ist das Baby {baby.alter} Jahre alt.")


""" 
Für Objekte wie Zahlen oder Zeichenketten gibt es Operatoren (wie +, * etc.) und Vergleichszeichen (wie ==, <= etc.)
Diese können auch für selber definierte Zahlen definiert werden. Dazu werden Funktionsnamen wie 
__add__  (für Addition)
__mul__ (für Multiplikation)
__eq__   (für Vergleich mit ==)
__le__   (für Vergleich mit <=)
verwendet.

Ein weiterer vorgegebener Methodenname ist auch __str__, welcher eine Zeichenketten-Darstellung des Objekts 
für Verwendung im print-Befehl zurückliefern soll.
""" 

class Bruch:
    def __init__(self,zaehler, nenner):
        self.zaehler=zaehler
        self.nenner=nenner
        if self.nenner==0:
            raise ValueError("0 darf nicht im Nenner stehen")
    
    def __eq__(self,other):
        return self.zaehler*other.nenner == self.nenner*other.zaehler
    
    def __mul__(self,other):
        return Bruch(self.zaehler*other.zaehler, self.nenner*other.nenner)
    
    def __str__(self):
        return f"{self.zaehler}/{self.nenner}"

# Rechnen mit Brüchen (Instanzen der Klasse Bruch)    

einHalbes = Bruch(1,2)
zweiDrittel = Bruch(2,3)
produkt = einHalbes * zweiDrittel
print(f"{einHalbes} * {zweiDrittel} = {produkt}") 
print(f"Ist das Produkt gleich 1/3? {produkt==Bruch(1,3)}")
print(f"Ist das Produkt gleich 5/7? {produkt==Bruch(5,7)}")
        