for i in range(4):  # 4 Wiederholungen; i geht von 0 bis 3    
    print("Hallo")

    
sum = 0
for n, u in enumerate(range(1,20,2)):     
    # Die 2 steht für die Schrittweite, u nimmt die Werte 1, 3, 5, ..., 19 an, n die Werte 0, 1, ..., 9
    print(f"Die {n+1}. ungerade Zahl lautet {u}.")
    sum += u
print(f"Die Summe aller ungeraden Zahlen kleiner als 20 beträgt {sum}.")

# Gib alle Augenpaare (i,j) mit i>=j aus    
for i in range(1,7):
    for j in range(1,i):
        print(f"({i},{j}) ")
        
        
inp = ""    
while inp!="Ende":
    inp = input("Möchten Sie noch was sagen? Sag 'Ende' um abzubrechen: ")
    print(f"Sie sagen: {inp}")

# Vorzeitiger Ausstieg aus Schleife mittels "break"
print("Du darfst dreimal raten, wie ich heisse. Wenn du es nicht errätst, gehört mir dein erstes Kind. ")
for i in range(1,4):
    antwort = input(f"Wie heisse ich? {i}. Versuch: ")
    if antwort=="Rumpelstilzchen":
        print("Das hat dir der Teufel gesagt!!")
        break

# Ausstieg aus Unendlich-Schleife
zahl = 7
print("Errate meine Lieblingszahl")
while True:
    tipp = int(input("Tipp: "))
    if tipp==zahl:
        print("Gratuliere. Du hast meine Lieblingszahl erraten!")
        break
    
