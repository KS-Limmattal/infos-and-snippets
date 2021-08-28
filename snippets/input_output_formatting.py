# Ausgabe, Eingabe und Formattierung

name = input("Wie heisst du? ")                                 # Input als Zeichenkette (string)
age = int(input("Wie alt bist du (in Jahren)? "))               # Input als Ganzzahl (int) interpretiert
height1 = float(input("Wie gross bist du (in cm)? "))           # Input als Fliesskommazahl (float) interpretiert
height2 = float(input("Wie gross warst du bei der Geburt (in cm)? "))

print(f"{name}, pro Lebensjahr bist du durchschnittlich {(height1-height2)/age:.2f} cm gewachsen") # Formattierung als f-string; Ausgabe auf 2 Nachkommastellen
