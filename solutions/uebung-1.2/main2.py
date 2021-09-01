"""
In dieser Aufgabe geht es um den Wurf von 3 Würfeln und Wahrscheinlichkeiten für eine bestimmte Augensumme

Schreiben Sie ein Programm mit folgender Eingabe/Ausgabe:
Eingabe: Augensumme (Zahl zwischen 3 und 18)
Ausgabe: Eine Liste aller Tripel (i,j,k), wobei i,j,k für die Augenzahlen von drei Würfeln mit der eingegebenen Augensumme stehen. 
         Geben Sie auch die Wahrscheinlichkeit (als Bruch) aus, dass die Augensumme die eingegebene Zahl beträgt
Bsp: (6,6,3), (6,5,4), (6,4,5), (6,3,6), (5,6,4), (5,5,5), (5,4,6), (4,6,5), (4,5,6), (3,6,6)
     Die Wahrscheinlichkeit für Augensumme 15 beträgt p = 10/216

Zusatz: Geben Sie die Tripel verteilt über mehrere Zeilen aus, so dass auf jeder Zeile Tripel stehen, die sich durch Permutation der Einträge auseinander ergeben.
"""

anzahl = 0
summe = int(input("Was soll die Augensumme der drei Würfel sein (min: 3, max:18): "))

for i in range(6,0,-1):
    for j in range(6,0,-1):
        for k in range(6,0,-1):
            if i+j+k==summe:
                print(f"({i},{j},{k})")
                anzahl+=1
print(f"Die Wahrscheinlichkeit für Augensumme {summe} beträgt p={anzahl}/216 ")