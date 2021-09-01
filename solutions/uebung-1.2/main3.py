"""
Schreiben Sie ein Programm mit folgender Eingabe/Ausgabe:
Eingabe: Eine natürliche Zahl
Ausgabe: "Die Zahl ... ist eine Primzahl" bzw. "Die Zahl ... ist keine Primzahl, denn sie hat den nicht-trivialen Teiler ..."

Zusatz: Versuchen Sie die Laufzeit des Programms zu optimieren
"""

prim = True
n = int(input("Geben Sie eine natürliche Zahl ein: "))

for t in range(2,n):
    if n%t==0:
        prim=False
        print(f"Die Zahl {n} ist keine Primzahl, denn sie hat den nicht-trivialen Teiler {t}.")
        break

if prim:
    print(f"Die Zahl {n} ist eine Primzahl")