#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import main2

"""
Diese Datei darf nur durch die Lehrperson abgeändert werden!
Sie wird für automatische Tests der Lösungen verwendet.
"""

def test():
    li1 = ["doppelt", "Aare", "Ananas", "Stein"]
    main2.streicheVerdoppelte(li1)
    assert li1 == ["Aare", "Ananas", "Stein"]
  
    li2 = ["Anna", "Stefan", "Klara", "Betti"]
    main2.streicheVerdoppelte(li2)
    assert li2 == ["Stefan", "Klara"]
  
    li3 = ["Wochentag", "Suppe", "stehen", "Wille", "Kino"]
    main2.streicheVerdoppelte(li3)
    assert li3 == ["Wochentag", "stehen", "Kino"]
  
    li4 = ["Michael", "Kurt", "Rebekka"]
    main2.streicheVerdoppelte(li4)
    assert li4 == ["Michael", "Kurt"]
    
    li5 = []
    main2.streicheVerdoppelte(li5)
    assert li5 == []
  
    
    li6 = ["keine", "verdopPelung", "haha", "Aua", "Aare"]
    main2.streicheVerdoppelte(li6)
    assert li6 == ["keine", "verdopPelung", "haha", "Aua", "Aare"]
    
    li7 = ["Aha", "Glosse", "Karikatur"]
    main2.streicheVerdoppelte(li7)
    assert li7 == ["Aha", "Karikatur"]

    li8 = ["Aha", "Gloria", "Karikatur"]
    main2.streicheVerdoppelte(li8)
    assert li8 == ["Aha", "Gloria", "Karikatur"]
