# Funktion wie in der Mathematik

def f(n):
    return n**2+3*n+1

# Funktionsaufruf
a = f(10)
print(a)

# Die selbe Funktion kann auch für andere Datentypen aufgerufen werden, sofern die Funktionsanweisungen dafür Sinn machen
import numpy as np
matrix = np.array([[1,2],[3,4]])
A = f(matrix)
print(A)


# Funktion mit mehreren Rückgabe-Anweisungen (nur die erste angetroffene wird ausgeführt)

def g(n):
    if n>0:
        return n**0.5
    elif n<0:
        return n**2
    
    return 42

print(g(2))
print(g(-1))
print(g(0))


# Kommentierung des Datentyps

def h(n: int) -> float:
    return n/4

print(h(7))
print(h(8))
# Der Funktion h soll nur eine Ganzzahl (int) übergeben werden, keine Matrix oder dergleichen

""" 
Allgemeiner: Eine Funktion in Python ist eine Folge von Anweisungen, die optional einen oder mehrere Werte 
             an den Aufrufer zurückliefern. Der Funktion können 0 oder mehr Argumente übergeben werden, 
             die in der Ausführung der Funktion verwendet werden können.
"""

# Funktion ohne Argument und ohne Rückgabewert
def sagHallo():
    print("Hallo!")
    
sagHallo()

# Funktion mit mehreren Argumenten und ohne Rückgabewert
def mehrfachAusgabe(s: str, n: int):
    for i in range(n):
        print(f"{i+1}. {s}")
        
mehrfachAusgabe("Text zum Wiedergeben", 7)

# Funktion mit einem Argument und mit mehreren Rückgabewerten

def spurUndDeterminante(A):
    return np.matrix.trace(A), np.linalg.det(A)

A = np.array([[1,2], [1,-3]])
spur, det = spurUndDeterminante(A)
print(f"Die Matrix \n {A} \n hat Spur {spur} und Determinante {det:.2f}")


""""
Bemerkung: Aus Gründen der Lesbarkeit ist es besser, die Rückgabe so früh wie möglich zu tätigen 
           und nicht zuerst in einer Variable abzuspeichern und erst am Schluss zurückzugeben
"""

def tuDiesNicht(n):
    werteListe = []
    if n<0:
        werteListe = ["Negatives Argument"]
    else:
        for i in range(n):
            werteListe.append(f"Zeichenkette {i+1}")
    return werteListe

print(tuDiesNicht(3))

def tuBesserDies(n):
    if n<0:
        return(["Negatives Argument"])
    else:
        werteListe = []
        for i in range(n):
            werteListe.append(f"Zeichenkette {i+1}")
        return werteListe

print(tuBesserDies(3))


"""
Verwendung von Variablen:
    - Variablen, die ausserhalb des Funktionsblocks (vor dem Aufruf der Funktion) definiert werden können
      von der Funktion verwendet werden.
    - Wird in einer Funktion eine Variable definiert, so kann sie normalerweise ausserhalb der Funktion
      nicht verwendet werden (lokale Variable), selbst wenn ausserhalb der Funktion eine (globale) Variable
      mit demselben Namen existiert
    - Soll in einer Funktion eine Wertzuweisung an eine globale Variable erfolgen, so muss dafür das
      Schlüsselwort "global" verwendet werden
"""  
      
def demo():
    x = 10   # lokale Variable
    print(f"Der Wert der lokalen Variable x ist {x}")
    global y
    print(f"Die globale Variable y hat zuerst den Wert {y}")
    y = 30
    global z
    z = "Dies ist eine in einer Funktion definierte globale Variable"

x = 20  # globale Variable  
y = 15  # globale Variable
w = "ab"
demo()
print(f"Der Wert der globalen Variablen x ist immer noch {x}")
print(f"Der Wert der globalen Variablen y ist neu {y}")
print(z) # Ausgabe einer in demo() definierten globalen Variablen
