#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ersetzen Sie in den folgenden Funktionen den behelfsmässigen 'pass' Befehl mit den passenden Anweisungen.
"""

def paritaetswechsel(li):
    """
    Zöhlt die Anzahl Paritätswechsel (gerade -> ungerade oder ungerade -> gerade) in einer Liste von ganzen Zahlen
    Beispiel 1: Die Liste [3, 4, 4, 8, 9, 7, -3, 15, 4] hat 3 Paritätswechsel (3->4, 8->9, 15->4)
    Beispiel 2: Die Liste [1, -3, 5, -1, 17, 31] hat 0 Paritätswechsel
        
    :param li: eine Liste bestehend aus ganzen Zahlen (Typ int)
    :return: die Anzahl der Paritätswechsel
    """
    anzahl = 0
    for i in range(len(li)-1):
        if (li[i]-li[i+1]) % 2 == 1:
            anzahl += 1
    return anzahl

def fibonacciSumme(n):
    """
    Gibt die Summe der ersten n Fibonacci-Zahlen zurück. 
    Erinnerung: Die Folge der Fibonacci-Zahlen beginnt mit 1, 1, 2, 3, 5, 8, 13, ...
    Beispiel: Zu n = 4 gehört der Rückgabewert 7 (dies ist 1+1+2+3)
        
    :param n: die Anzahl der Fibonacci-Zahlen, die aufsummiert werden sollen (n>=1)
    :return: die Summe dieser Fibonacci-Zahlen
    """
    
    if n==1:
        return 1
    
    fib1 = 1
    fib2 = 1
    summe = fib1+fib2
    
    for i in range(n-2):
        tmp = fib1 + fib2
        fib1 = fib2
        fib2 = tmp
        summe += fib2
        
    return summe