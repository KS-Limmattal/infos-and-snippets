#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import main2

"""
Diese Datei darf nur durch die Lehrperson abgeändert werden!
Sie wird für automatische Tests der Lösungen verwendet.
"""

def test():
    assert main2.palindrome(["Aha", "Echo", "Anna", "Rentner", "gaga"]) == ["Aha", "Anna", "Rentner"]
    assert main2.palindrome(["Palindrom", "haiah"]) == ["haiah"]
    assert main2.palindrome(["Hier", "gibt", "es", "kein", "Palindrom"]) == []
    assert main2.palindrome([]) == []
