#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import main1 as sol

"""
Diese Datei darf nur durch die Lehrperson abgeändert werden!
Sie wird für automatische Tests der Lösungen verwendet.
"""

def test():
    fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for n in range(1, len(fib) + 1):
        assert sol.fibonacciSumme(n) == sum(fib[:n])