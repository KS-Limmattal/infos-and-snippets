s1 = "Dies ist eine Zeichenkette"
s2 = 'Das geht auch'
s3 = 'Die Programmiersprache "Python"'                 # wenn Python in "" geschrieben sein soll
s4 = "Die Programmiersprache 'Python'"                 # wenn Python in '' geschrieben sein soll

print(s3)
print(s4)

s5 = s1 + s2                                           # Verettung (Hintereinanderschaltung) zweier Zeichenketten
len(s5)                                                # Länge einer Zeichenkette


s6 = '''Lange Zeichenkette, die über mehrere
Zeilen verteilt ist'''

s7 = 5*s1                                             # Dasselbe wie s1 + s1 + s1 + s1 + s1 (Verkettung)

s8 = s1.lower()                                       # Alles kleingeschrieben
s9 = s1.upper()                                       # Alles grossgeschrieben

s10 = s1.split()                                      # Liste der auftretenden Wörter