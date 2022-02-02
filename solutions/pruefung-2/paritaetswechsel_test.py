#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import main1 as sol

"""
Diese Datei darf nur durch die Lehrperson abgeändert werden!
Sie wird für automatische Tests der Lösungen verwendet.
"""

def test():
    assert sol.paritaetswechsel([3, 4, 4, 8, 9, 7, -3, 15, 4]) == 3
    assert sol.paritaetswechsel([1]) == 0
    assert sol.paritaetswechsel([]) == 0
    assert sol.paritaetswechsel([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 8
    assert sol.paritaetswechsel([10, 20, 30, 40, 50, 60, 70, 80, 90]) == 0
    assert sol.paritaetswechsel([1, 3, 5, 7, 9, 2, 4, 6, 8]) == 1
    assert sol.paritaetswechsel([1, 2, 4, 6, 8, 10, 12, 14, 15]) == 2