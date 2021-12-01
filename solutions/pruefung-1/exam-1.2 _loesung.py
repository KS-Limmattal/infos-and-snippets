#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prüfungsaufgabe 2 (vom 24.11.2021)

Schreiben Sie ein Programm, welches dem Benutzer erlaubt, eine komplexe 2x2 Matrix einzugeben.
Geben Sie dann in einem Satz aus, ob die Matrix invertierbar ist und geben Sie im Falle der
Invertierbarkeit die Inverse der Matrix aus.
"""

import numpy as np
A = np.zeros((2,2))+0*1j
A[0,0] = complex(input("a11 = "))
A[0,1] = complex(input("a12 = "))
A[1,0] = complex(input("a21 = "))
A[1,1] = complex(input("a22 = "))

if np.linalg.det(A)!=0: 
    inv = np.linalg.inv(A)
    print(f"Die Matrix \n {A} \n ist invertierbar mit Inverse \n {inv}")
else:
    print(f"Die Matrix \n {A} \n ist nicht invertierbar")