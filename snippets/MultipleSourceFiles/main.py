#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
main.py ist das auszuführende Skript
module1, module2, module3 sind zu importierende Module
module2 und module3 befinden sich im Unterordner subfolder

Die Zerlegung eines grösseren Projekts in mehrere Dateien führt nicht nur zu mehr Übersichtlichkeit im Code, 
sondern auch zu einfacherer Zusammenarbeit untereinander. Werden nämlich in verschiedenen Pull Requests 
verschiedene Dateien verändert, so gibt es garantiert keine Probleme (merge conflict) bei der Zusammenführung.
"""

from module1 import welcome
from subfolder.module2 import Vector3d
from subfolder.module3 import Point3d, pointInput

welcome()
p1 = pointInput("Geben Sie die Koordinaten eines ersten Punkts ein.")
p2 = pointInput("Geben Sie die Koordinaten eines zweiten Punkts ein.")

print(f"Der Abstand der Punkte {p1} und {p2} beträgt {p1.dist(p2)}")

print()
p = pointInput("Geben Sie einen Punkt ein. ")
v = Vector3d(p.x,p.y,p.z)
print(f"Der Ortsvektor von {p} lautet {v}")
