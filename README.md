# Installation

## MS Windows
.
Empfohlen wird die portable Python-Installation [WinPython](https://github.com/winpython/winpython), Version 3.9.5. vom 4. Juli 2021 Diese enthält alle Module (inklusive math, cmath, numpy, pygame), die wir in diesem Semester benötigen werden. WinPython enthält die Python-Programmierumgebung Spyder, mit der wir arbeiten werden.

Für eine leistungsfähige Konsole und Arbeit mit `Git`-Repositories wird [PortableGit](https://github.com/git-for-windows/git) empfohlen, Version 2.33.0.2 vom 17. August 2021. 

PortableGit soll in einen Ordner `PortableGit` im Ordner installiert werden, in welchem bereits WinPython installiert ist (z.B. im Wurzel-Verzeichnis `D:` oder `E:` für ein USB-Stick). Git wird mittels der
Kommandozeile `git-bash` verwendet. Um `gitbash` direkt aus dem Ordner auszuführen, welches `WinPython` und `PortableGit` enthält, wird am besten von `git-bash.exe` mittels Rechtsklick "Verknüpfung erstellen" eine Verknüpfung erstellt. Die Verknpüfung wird nun ins Verzeichnis mit `WinPython` und `PortableGit` verschoben. Ausserdem erstellen wir in diesem Verzeichnis einen Ordner `MyCode`, in welcher der eigene Python Code platziert wird.

Die Ordner-Struktur sollte nun wie folgt aussehen:
![grafik](https://user-images.githubusercontent.com/40485433/131446510-0f393315-001b-4161-b1a6-75ff74f86606.png)

Durch Rechtklick auf die Verknüpfung auf `git-bash.exe` können wir das Verzeichnis, in welchem das Terminal gestartet wird, auf unser eigenes Code-Verzeichnis setzen:
![grafik](https://user-images.githubusercontent.com/40485433/131446801-2b9c42b5-4374-43c9-8c7e-01e20851b617.png)

## MacOS

Python3 und pip3 sind üblicherweise vorinstalliert. Die Programmierumgebung `spyder` erhält man auf [der Spyder Installationsseite](https://docs.spyder-ide.org/current/installation.html)

Ein Terminal gibt es unter MacOS vorintalliert. Um `Git` zu installieren, kann man im Terminal `git` eingeben und wird durch die Installation geführt.

## Linux

Sowohl `python3`, der Paket-Installer `pip3` wie auch die Programmierumgebung `spyder` sowie `git` lassen sich über die Kommandozeile installieren (unter Ubuntu `sudo apt install python3 pip3 spyder git`)

## Online Editoren

- [Python Tutor](https://pythontutor.com/)
- [Online Python](https://www.online-python.com/)

# Arbeit mit Git

`Git` ist ein leistungsfähiges Versionskontroll-System, welches besonders gut beim Programmieren eingesetzt werden kann.
Gerade bei Zusammenarbeit von mehreren ProgrammiererInnen ist ein Versionskontroll-System unabdingbar, da so mehrere Personen
unabhängig am gleichen Projekt arbeiten können. Es bietet aber auch für einzelne ProgrammiererInnen viele Vorteile. 
Zum Beispiel lassen sich Änderungen an den Teilen des Projekts schnell inspizieren, modifizieren oder rückgängig machen.
Ausserdem kann an verschiedenen Projekt-Features unabhängig gearbeitet werden.

Jedes Programmierprojekt wird in einem `Repository` abgelegt. Dies ist ein virtueller Speicher, welches aus der Kollektion 
der Dateien des Projekts und Metadata zur Versionskontrolle besteht. Jede substanzielle Code-Änderung 
wird in einem `Commit` zur Projekt-Geschichte hinzugefügt und mit einer Überschrift betitelt.
`Github` ist ein internet-basierter Dienst zum Einsatz von `Git`. Beginnt man `Github` zu verwenden, sind einige Konfigurationsschritte nötig,
die im folgenden [Video](https://www.youtube.com/watch?v=kHkQnuYzwoo) erklärt werden. Eine weitere empfehlenswerte Einstellung lautet:
```
git config --global pull.rebase true
```

Die Projekt-Geschichte lässt sich mittels 
```
git log
```
anzeigen. Zum Beispiel sieht die Projekt-Geschichte zum infos-and-snippets Repository momentan wie folgt aus:

![grafik](https://user-images.githubusercontent.com/40485433/131213722-0036b625-5480-4bc8-9c74-214081c4cc6d.png)

Es ist daraus also ersichtlich, wer wann welche Commits gemacht hat und was damit bezweckt werden sollte.


# Aufgaben
- [Aufgabe 1](https://classroom.github.com/a/UNwqoiUj)
- [Aufgabe 2](https://classroom.github.com/a/c8MHVeSV)

# Themen

## 1. Teil 
- Eingabe und Ausgabe
- Textformattierung (f-Methode)
- if-Abfrage
- Schleifen (while, for)
