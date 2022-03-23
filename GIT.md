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
die im folgenden [Video](https://www.youtube.com/watch?v=kHkQnuYzwoo) erklärt werden. Weitere empfehlenswerte Einstellungen lauten:
```
git config --global pull.rebase true
```
und

```
git config --global credential.helper manager-core
```

## Projekt-Geschichte

Die Projekt-Geschichte lässt sich mittels 
```
git log
```
anzeigen. Zum Beispiel hat die Projekt-Geschichte zum infos-and-snippets Repository mal wie folgt ausgesehen:

![grafik](https://user-images.githubusercontent.com/40485433/131213722-0036b625-5480-4bc8-9c74-214081c4cc6d.png)

Es ist daraus also ersichtlich, wer wann welche Commits gemacht hat und was damit bezweckt werden sollte.

## Aktueller Zustand

Der aktuelle Zustand des Git Repositories lässt sich mittels
```
git status
```
anzeigen. Hier wird ersichtlich, ob es geänderte Dateien gibt, ob diese bereits für einen neuen Commit vorgemerkt sind (grün statt rot) und ob gerade ein
"Merge" oder "Rebase" Prozess zur Zusammenführung von Dateien im Gange ist. Ausserdem wird der aktuelle Branch (Zweig) angezeigt, auf welchem gearbeitet wird.

Zum Beispiel zeigt:
```
Auf Branch main
Ihr Branch ist auf demselben Stand wie 'origin/main'.

Änderungen, die nicht zum Commit vorgemerkt sind:
  (benutzen Sie "git add <Datei>...", um die Änderungen zum Commit vorzumerken)
  (benutzen Sie "git restore <Datei>...", um die Änderungen im Arbeitsverzeichnis zu verwerfen)
	geändert:       snippets/loops.py

Unversionierte Dateien:
  (benutzen Sie "git add <Datei>...", um die Änderungen zum Commit vorzumerken)
	other/

keine Änderungen zum Commit vorgemerkt (benutzen Sie "git add" und/oder "git commit -a")
```
an, dass auf dem Hauptzweig `main` gearbeitet wird und dass es eine geänderte Datei `snippets/loops.py` gibt, die mittels `git add snippets/loops.py` 
für einen Commit vorgemerkt werden kann. Auch das Verzeichnis `other/` ist neu und kann hinzugefügt werden.

## Klonen von Repositories

Um ein Repository vom Online-Dienst Github zu klonen, verwendet man den Befehl `git clone`. Bei fremden Repositories empfiehlt sich, diese zuerst 
mittels `Fork` abzuzweigen, so dass man die abgezweigte Variante nicht nur lokal, sondern auch auf Github verändern kann. Ohne Abzweigung 
fehlt die Berechtigung dazu. 

Um etwa das `info-and-snippets` repository zu klonen, gehst du auf [https://github.com/KS-Limmattal/infos-and-snippets](https://github.com/KS-Limmattal/infos-and-snippets)
und klickst rechts oben auf `Fork`. 
Dann tippe im gewünschten Verzeichnis in der Konsole, in welcher du `git` ausführen kannst:
```
git clone https://github.com/KS-Limmattal/infos-and-snippets.git
```
## Zweig erstellen und auschecken

Soll ein neues feature oder ein neuer bugfix erstellt werden, so geschieht die Entwicklung in einem neuen `branch` (niemals im `main` branch).
Das Erstellen und Auschecken lässt sich in einem einzigen Befehl schreiben:

```
git checkout -b <branchname>
```
Achte darauf, dass du dich vorher auf dem `main` branch befindest, denn sonst wird von einem anderen `branch` abgezweigt.

## Änderungen bereitstellen und veröffentlichen

Anstatt die neusten Code-Dateien auf Github im Web-Interface reinzukopieren und so zu veröffentlichen, lautet der Ablauf aus der Kommandozeile wie folgt:

```
git add <Dateiname(n)>
git commit -m "Commit-Nachricht"
git push
```
Dabei sollte im Zweifelsfall vorher mittels
```
git fetch --all
git status
```
überprüft werden, ob der aktuelle Zweig im lokalen Repository im selben Zustand wie das Online Repository ist und ob man sich auf dem richtigen `branch` befindet (es sollte beim pushen insbesondere niemals der `main` branch sein).

## Pull Request erzeugen und annehmen

Hat man den feature- oder bugfix-branch aufs Remote Repository gepusht, so kann man auf Github (unter `Pull Requests`) nun einen Pull Request erzeugen `Compare & Create Pull Request`. Diesen können Gruppenmitglieder studieren und bei Einverständnis aller Gruppenmitglieder in den `main` branch integrieren. Verwende dazu `Rebase and Merge` im Web-Interface. Der `main` branch sollte immer in funktionablem Zustand sein. 

## Änderungen vom Remote Repository herunterladen

Wenn man einen neuen Zweig erstellt und daran arbeitet, so ist es häufig der Fall, dass der Zweig `main`, von welchem damals abgezweigt wurde, nicht mehr den neuesten Stand widerspiegelt, weil inzwischen schon einige `commits` zum `main` branch auf dem Remote Repository hinzugeüfgt worden sind. Möchte man diese Änderungen in den aktuellen Zweig integrieren, so geht das mit 

`` 
git rebase origin/main
```
