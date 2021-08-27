# Installation

## MS Windows

Empfohlen wird die portable Python-Installation [WinPython](https://github.com/winpython/winpython), Version 3.9.5. vom 4. Juli 2021. Diese enthält alle Module (inklusive math, cmath, numpy, pygame), die wir in diesem Semester benötigen werden. WinPython enthält die Python-Programmierumgebung Spyder, mit der wir arbeiten werden.

Für eine leistungsfähige Konsole und Arbeit mit `Git`-Repositories wird der portable [Cmder](https://github.com/cmderdev/cmder/) empfohlen, Version 1.3.18 vom 26. März 2021. 

WinPython und der Cmder sollen ins gleiche Verzeichnis extrahiert werden (z.B. das Wurzel-Verzeichnis `D:` oder `E:` für ein USB-Stick). Ausserdem soll in das Verzeichnis `cmder\bin\` die [winpy.bat](https://raw.githubusercontent.com/KS-Limmattal/infos-and-snippets/main/winpy.bat) Datei reinkopiert werden, damit WinPython mit Git verbunden wird. Doppelklick auf `winpy.bat` im Datei-Manager sollte nun eine Konsole öffnen, in welcher auch `git` verfügbar ist.

![grafik](https://user-images.githubusercontent.com/40485433/131105413-4bb5b956-cf09-49db-a99f-0b31dc44a3d7.png)

Um `winpy.bat` direkt im Verzeichnis auszuführen, welches WinPython und Cmder enthält, wird am besten in `\cmder\bin\` mittels Rechtsklick "Verknüpfung erstellen" eine Verknüpfung zu `winpy.bat` erstellt. Die Verknpüfung wird nun ins Verzeichnis mit WinPython und Cmder verschoben. Ausserdem erstellen wir in diesem Verzeichnis einen Ordner `MyCode`, in welcher der eigene Python Code platziert wird.

Die Ordner-Struktur sollte nun wie folgt aussehen:
![grafik](https://user-images.githubusercontent.com/40485433/131106065-ccaf28fd-67cb-431a-a7ca-965f2c93d520.png)

Durch Rechtklick auf die Verknüpfung auf winpy.bat können wir das Verzeichnis, in welchem das Terminal gestartet wird, auf unser eigenes Code-Verzeichnis setzen:
![grafik](https://user-images.githubusercontent.com/40485433/131131491-02db0183-45ad-49c1-adb3-4c65fbd4087f.png)


## MacOS

Python3 und pip3 sind üblicherweise vorinstalliert. Die Programmierumgebung `spyder` erhält man auf [der Spyder Installationsseite](https://docs.spyder-ide.org/current/installation.html)

Ein Terminal gibt es unter MacOS vorintalliert. Um `Git` zu installieren, kann man im Terminal `git` eingeben und wird durch die Installation geführt.

## Linux

Sowohl `python3`, der Paket-Installer `pip3` wie auch die Programmierumgebung `spyder` sowie `git` lassen sich über die Kommandozeile installieren (unter Ubuntu `sudo apt install python3 pip3 spyder git`)

## Online Editoren

- [Python Tutor](https://pythontutor.com/)
- [Online Python](https://www.online-python.com/)

# Aufgaben
- [Aufgabe 1](https://classroom.github.com/a/UNwqoiUj)

# Themen

## 1. Teil 
- Eingabe und Ausgabe
- Textformattierung (f-Methode)
- if-Abfrage
- Schleifen (while, for)
