"""
Eine Zahl zwischen 1 und 1'000'000 soll erraten werden.

Schreiben Sie ein Programm, welches den Benutzer wiederholt mit Fragen der Art "Ist die Zahl grösser als ... (j/n)" konfrontiert und 
damit die vom Benutzer ausgedachte Zahl errät.
Beginnen Sie mit einer Ausgabe, welche den Benutzer auffordert, sich eine Zahl zwischen 1 und 1'000'000 auszudenken.

Zusatz: Finden Sie heraus, wie viele Fragen das Programm optimalerweise im schlimmsten Fall mindestens stellen muss, 
        um das Ergebnis zu erhalten.
"""

print("Denken Sie sich eine Zahl zwischen 1 und 1'000'000 aus. ")
inp = ""
minimum = 1
maximum = 1000
while maximum != minimum:
    tipp = (minimum + maximum) // 2          # Mittelwert abgerundet
    inp=input(f"Ist die Zahl grösser als {tipp} (j/n): ")
    if inp=="j":
        minimum=tipp+1
    else:
        maximum=tipp
    print(f"max: {maximum}, min: {minimum}")
        
print(f"Die gesuchte Zahl ist {minimum}")
    