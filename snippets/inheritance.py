#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Haben mehrere Code-Teile Gemeinsamkeiten, so können wir diese in eine Funktion auslagern, die von
den usprünglichen Code-Teilen aufgerufen werden.

Haben mehrere Klassen Gemeinsamkeiten, so können wir diese in einer Klasse auslagern, von der die
usprünglichen Klassen erben.

Die erbenden Klassen heissen Oberklassen (superclasses). Sie erben alle Eigenschaften und Methoden
der Unterklasse (subclass). Vererbte Methoden können aber auch überschrieben werden.
"""

class Unterklasse:
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        print("Unterklassen __init__")
    
    def methode1(self):
        print("Diese Methode ist in der Unterklasse definiert")
    
    def methode2(self, dx):
        print("Auch diese Methode ist in der Unterklasse definiert")
        self.x += dx
        print(f"Das neue x ist {self.x}")
        
class Oberklasse1(Unterklasse):                   # In Klammern steht die Klasse, von der geerbt wird
                                                  # Es kann auch von mehreren Klassen geerbt werden
                                                  # Die Unterklassen müssen durch Kommas separiert werden.
    
    def __init__(self, x, y, z, a, b):
        super().__init__(x,y,z)                   # Rufe __init__ Methode der Unterklasse auf
        self.a = a                                # Zusätzliche Eigenschaften der Oberklasse1
        self.b = b
        print("Oberklassen1 __init__")
        
    def methode3(self):
        print("Diese Methode ist in der Oberklasse1 definiert")
        
    def methode2(self, dx):
        print("Diese Methode ist von der Oberklasse1 überschrieben")
        self.x -= 2*dx
        print(f"Das neue x ist {self.x}")
        
class Oberklasse2(Unterklasse):
    
    def __init__(self,x,y,z, u):
        super().__init__(x,y,z)
        self.u = u                               # Zusätzliche Eigenschaft der Oberklasse2
        print("Oberklassen2 __init__")

    def methode4(self):
        print("Diese Methode ist in der Oberklasse2 definiert")
        

uk = Unterklasse(5,17,4)
ok1 = Oberklasse1(2,7,8, "Hallo", 4)
ok2 = Oberklasse2(13,2,4, [3.1, 3.14, 3.15])
 
uk.methode1()
uk.methode2(10)

ok1.methode3()
ok1.methode1()
ok1.methode2(10)

ok2.methode4()
ok2.methode1()
ok2.methode2(10)