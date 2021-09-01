"""
Schreiben Sie ein Programm mit folgender Eingabe/Ausgabe 
Eingabe: Vorname, Nachname, Geschlecht (m/f)
Ausgabe:"Guten Tag Herr ... ..." bzw. "Guten Tag Frau ... ..." (mit Vorname und Nachname)

Zusatz: Verwenden Sie f-string Formattierung bei der Ausgabe und benützen Sie dabei Variablen vorname, nachname, anrede von Typ str
"""

vorname=input("Geben Sie Ihren Vornamen ein: ")
nachname=input("Geben Sie Ihren Nachnamen ein: ")
geschlecht=input("Geben Sie Ihr Geschlecht (m/f) ein: ")

anrede = "Herr" if geschlecht=="m" else "Frau"
print(f"Guten Tag {anrede} {vorname} {nachname}")
