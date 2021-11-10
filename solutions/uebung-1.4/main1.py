#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Erstelle ein Wörterbuch (dictionary), welches dem Kürzel jeder Fachlehrperson der Klasse M5a den vollen Namen zuordnet
(z.B. 'loe' wird zu 'Roland Lötscher')
Erzeuge danach daraus eine Liste aller Kürzel der Namen der Fachlehrpersonen, welche einen Umlaut enthalten.
"""

name = {
        'loe':'Roland Lötscher',
        'lep': 'Marco Lepori',
        'leu': 'Barbara Leuenberger'
}

list = [k for k in name.keys() if "ö" in name[k] or "ü" in name[k] or "ä" in name[k]]