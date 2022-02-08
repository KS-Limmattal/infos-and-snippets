#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Das Ziel dieser Übung besteht darin, das Pong-Spiel von https://www.python-lernen.de/pygame-kollisions-kontrolle.htm
objektorient (unter Verwendung von Klassen für Ball und Schläger) umzuschreiben. Gehen Sie dazu wie folgt vor:

1) Testen Sie zuerst das oben verlinkte Spiel ausgiebig aus und versuchen Sie den Code zu verstehen. 
   Spielen Sie mit dem Code rum, testen Sie Änderungen von Variablen-Werten aus.

2) Starten Sie nun neu mit dem Grundgerüst für pygame-Spiele in den snippets.

3) Definieren Sie eine Klasse namens "Ball" mit folgenden Eigenschaften und Methoden:
    - Eigenschaften: x, y (Position), vx, vy (Geschwindigkeit), d (Durchmesser)
    - Methoden: 
        __init__
        draw (zum Zeichnen des Balls)

4) Definieren Sie eine Klasse namens "Schlaeger" mit folgenden Eigenschaften und Methoden:
    - Eigenschaften: x, y (Position), 
                     bewegung (um wieviele Pixel der Schläger pro Zeiteinheit bewegt wird) 
                     tasteHoch, tasteRunter (für die Tasten, die für die Bewegung des Schlägers verwendet werden sollen)
                     start (Position des Balls, wenn er den Schläger verpasst hat und zurückgesetzt wird)
                     hoehe (aktuelle Höhe des Schlägers)
                     score (aktuelle Punktzahl des Spielers, der den Schläger steuert)
                           im Unterschied zum originalen Spiel sollen nicht die Ballwechsel gezählt werden, 
                           sondern jede Ballberührung gibt einen Punkt für den entsprechenden Spieler
    - Methoden: __init__
                draw (zum Zeichnen des Schlägers)
                
5) Erstellen Sie eine Instanz der Klasse "Ball", sowie eine Liste bestehend aus zwei Instanzen der Klasse "Schlaeger",
    mit Werten, die dem originalen Pong-Spiel entsprechen
    
6) Fügen Sie Code ein für:
    - die Setzung der "bewegung" Eigenschaft bei Tastendruck hoch/runter
    - die Aktualisierung der Positionen von Ball und Schlägern
    - das Zeichnen von Ball und Schlägern
    - die Reaktion auf Zusammenstoss von Ball mit einem Schläger
    - die Ausgabe des Zwischenstands
"""

# Importieren und initialisieren des pygame-Moduls
import pygame
from pygame.locals import *
pygame.init()

# Variablen/KONSTANTEN setzen
FENSTERBREITE, FENSTERHOEHE = 480, 640
FPS  = 60   # angepeilt werden ebenso viele Bildschirmaktualisierungen pro Sekunde.
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)

# Hilfsfunktionen und Klassen definieren (z.B. für Spieler, Gegner, Spielfeld etc.)

class Ball:
    def __init__(self, x, y, vx, vy, d): 
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.d = d
        
    def draw(self, screen):
        return pygame.draw.ellipse(screen, WEISS, [self.x, self.y, self.d, self.d])

class Schlaeger:
    def __init__(self, x, y, bewegung, tasteHoch, tasteRunter, start, hoehe=220, score=0):
        self.x = x
        self.y = y
        self.bewegung = bewegung
        self.tasteHoch = tasteHoch
        self.tasteRunter = tasteRunter
        self.start = start
        self.hoehe = hoehe
        self.score = score
        
    def draw(self, screen):
        return pygame.draw.rect(screen, WEISS, [self.x, self.y, 20, self.hoehe])

def clamp(x,min,max):
    if x < min:
        return min
    if x > max:
        return max
    return x

# Spielobjekte (Instanzen) erzeugen. Gleichartige Spielobjekte können in Listen abgelegt werden.

ball = Ball(50, 30, 4, 4, 20)

schlaegerListe = [Schlaeger(20, 20, 0, pygame.K_UP,pygame.K_DOWN, 40), 
                Schlaeger(FENSTERBREITE - 40, 20, 0, pygame.K_w,pygame.K_s, 400)]

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

        # Schlaegerbewegung rauf/runter    
        if event.type == pygame.KEYDOWN:
            print("Taste wurde gedrückt")
            for schlaeger in schlaegerListe:
                if event.key == schlaeger.tasteHoch:
                    schlaeger.bewegung = -6
                elif event.key == schlaeger.tasteRunter:
                    schlaeger.bewegung = 6

        # Stoppen der Schlaegerbewegung
        if event.type == pygame.KEYUP:
            print("Spieler hat Taste losgelassen")
            for schlaeger in schlaegerListe:
                if event.key == schlaeger.tasteHoch or event.key == schlaeger.tasteRunter:
                    schlaeger.bewegung = 0


    # Spiellogik (z.B. Bewegungen der Spieler)

    for schlaeger in schlaegerListe:
        schlaeger.y+=schlaeger.bewegung
        schlaeger.y=clamp(schlaeger.y, 0, FENSTERHOEHE - schlaeger.hoehe)
        
    ball.x+=ball.vx
    ball.y+=ball.vy
    if ball.x != clamp(ball.x, 0, FENSTERBREITE - ball.d):
        ball.vx *= -1
    if ball.y != clamp(ball.y, 0, FENSTERHOEHE - ball.d):
        ball.vy *= -1
        
        
    # Spielfeld löschen (mit weissem oder schwarzem Hintergrund)
    fenster.fill(SCHWARZ)

    # Aktualisiertes Spielfeld/Figuren zeichnen

    kreis = ball.draw(fenster)

    for schlaeger in schlaegerListe:
        rechteck = schlaeger.draw(fenster)
        if rechteck.colliderect(kreis):
            print("Zusammenstoß")
            ball.vx *= -1
            ball.x = schlaeger.start
            schlaeger.hoehe -= 5
            schlaeger.score += 1
            
    # Fenster aktualisieren
    pygame.display.flip()
    clock.tick(FPS)