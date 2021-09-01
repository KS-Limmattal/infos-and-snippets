"""
Schreiben Sie ein Programm, welches vom Benutzer wiederholt Notenwerte abfragt und am Schluss den Notendurchschnitt auf 2-Nachkommastellen gerundet ausgibt.

Zusatz: Überprüfen Sie die eingegebenen Notenwerte auf Plausibilität und erlauben Sie auch Komma statt Punkt als Dezimalpunkt
"""


summe = 0
anzahl = 0
while True:
    eingabe=input("Geben Sie einen Notenwert (z.B. 5.5) ein oder geben Sie 'Ende' ein, um die Noteneingabe zu beenden. \n >>> ")
    if eingabe=="Ende":
        break
    else:
        note = float(eingabe)
        summe += note
        anzahl += 1

if anzahl==0:
    print("Keine Noten eingegeben")
else:    
    print(f"Ihr Notenschnitt beträgt {summe/anzahl:.2f}")