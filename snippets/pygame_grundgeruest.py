#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dies ist ein Grundgerüst für Spiele, die das pygame-Modul verwenden.
Nach dem Initialiseren des Moduls wird eine Spielschleife (game loop) gestartet, 
welche nur durch Benutzer-Aktion (wie Esc, Schliessen des Fensters) beendet wird.
In der Spielschleife wird in regelmässigen zeitlichen Abständen auf die
Benutzereingaben reagiert und der Zustand der Spielobjekte sowie der Bildschirm 
aktualisiert.
"""

# Importieren und initialisieren des pygame-Moduls
import pygame
from pygame.locals import *
pygame.init()

# Variablen/KONSTANTEN setzen
FENSTERBREITE, FENSTERHOEHE = 800, 600
FPS  = 60   # angepeilt werden ebenso viele Bildschirmaktualisierungen pro Sekunde.
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)

# Hilfsfunktionen und Klassen definieren (z.B. für Spieler, Gegner, Spielfeld etc.)

# Spielobjekte (Instanzen) erzeugen. Gleichartige Spielobjekte können in Listen abgelegt werden.

# Definieren und öffnen eines neuen Fensters
fenster = pygame.display.set_mode((FENSTERBREITE, FENSTERHOEHE))
pygame.display.set_caption("Titel für Fensterkopf")

# Uhr wird zum regelmässigen Updaten der Graphik verwendet
clock = pygame.time.Clock()

# Spielschleife
while True:
    # Überprüfen, ob Benutzer eine Aktion durchgeführt hat. Dazu werden die Ereignisse (events) abgefragt:
    for event in pygame.event.get():
        # Beenden bei [ESC] oder [X]
        if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
            pygame.quit()

        # Weitere Reaktionen auf Benutzereingaben

    # Spiellogik (z.B. Bewegungen der Spieler)

    # Spielfeld löschen (mit weissem oder schwarzem Hintergrund)
    fenster.fill(WEISS)

    # Aktualisiertes Spielfeld/Figuren zeichnen

    # Fenster aktualisieren
    pygame.display.flip()
    clock.tick(FPS)