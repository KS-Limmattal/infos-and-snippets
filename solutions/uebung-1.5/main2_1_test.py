#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import main2

"""
Diese Datei darf nur durch die Lehrperson abgeändert werden!
Sie wird für automatische Tests der Lösungen verwendet.
"""

def test():
    assert main2.erstesR(["Roland", "Stefan", "Klara", "Ritalin", "Hans", "Gabriel"]) == "Roland"
    assert main2.erstesR(["Otto", "Stefan", "Klara"]) == "Klara"
    assert main2.erstesR(["Wochentag", "Suppe", "stehen", "Wille", "Kino"]) == ""
    assert main2.erstesR(["Michael", "Kurt", "Rebekka"]) == "Kurt"
    assert main2.erstesR([]) == ""