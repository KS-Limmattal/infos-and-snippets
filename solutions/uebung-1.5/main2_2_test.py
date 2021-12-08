#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import main2

"""
Diese Datei darf nur durch die Lehrperson abgeändert werden!
Sie wird für automatische Tests der Lösungen verwendet.
"""

def test():
    assert main2.letzteVerdopplung(["doppelt", "Aare", "Ananas", "Stein"]) == "doppelt"
    assert main2.letzteVerdopplung(["Anna", "Stefan", "Klara", "Betti"]) == "Betti"
    assert main2.letzteVerdopplung(["Wochentag", "Suppe", "stehen", "Wille", "Kino"]) == "Wille"
    assert main2.letzteVerdopplung(["Michael", "Kurt", "Rebekka"]) == "Rebekka"
    assert main2.letzteVerdopplung([]) == ""
    assert main2.letzteVerdopplung(["keine", "verdopPelung", "haha", "Aua", "Aare"]) == ""

    li1 = ["Aha", "Glosse", "Karikatur"]
    li1Copy = li1.copy()
    ret1 = main2.letzteVerdopplung(li1)
    assert ret1 == "Glosse"
    assert li1 == li1Copy

    li2 = ["Aha", "Gloria", "Karikatur"]
    li2Copy = li2.copy()
    ret2 = main2.letzteVerdopplung(li2)
    assert ret2 == ""
    assert li2 == li2Copy  