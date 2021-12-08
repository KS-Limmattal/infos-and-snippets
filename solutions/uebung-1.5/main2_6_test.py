#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import main2

"""
Diese Datei darf nur durch die Lehrperson abgeändert werden!
Sie wird für automatische Tests der Lösungen verwendet.
"""

def test():
    assert main2.teilbuch({'key1':'val1', 'key2': 'val2', 'key3': 'val3'}, ['key1', 'key2'])== {'key1':'val1', 'key2': 'val2'}
    assert main2.teilbuch({'a':1, 'b':5, 'c':2, 'd':11},['a', 'b', 'd', 'e']) == {'a':1, 'b':5, 'd':11}
    assert main2.teilbuch({'a':1, 'b':5, 'c':2, 'd':11},['c']) == {'c':2}
    assert main2.teilbuch({'a':1, 'b':5, 'c':2},['e','a',2]) == {'a':1}
    assert main2.teilbuch({'a':3, 'b':5, 'c':2},['x','y','z',3,5,2]) == {}
    assert main2.teilbuch({},['a','b']) == {}
    assert main2.teilbuch({'a':1, 'b':2, 'c':3},[]) == {}
