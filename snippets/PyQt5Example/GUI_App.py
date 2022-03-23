from PyQt5 import QtWidgets, uic

"""
Tutorial: https://nitratine.net/blog/post/how-to-import-a-pyqt5-ui-file-in-a-python-gui/

Ein Widget ist ein graphisches Element einer graphischen Benutzeroberfläche (GUI)
Die GUI-Bibliothek, die wir verwenden, heisst Qt (ausgesprochen "cute"), genauer PyQt5.
Bei Qt handelt es sich um eine freie quell-offene GUI-Bibliothek, welche auf allen grossen 
Plattformen inklusive Mobil-Plattformen verwendet werden kann.

Die GUI kann mit QtDesigner relativ bequem erzeugt werden.
Die Interatkion mit dem Benutzer wird im Code festgelegt. Die in QtDesigner erzeugte .ui-Datei
wird dabei mit Hilfe von PyQt5.uic (Befehl uic.loadUi) eingebunden. 
Dies geschieht dadurch, dass eine Superklasse vom Qt-Widget erzeugt wird, welche dem Form Typ
entspricht, die in Qt-Designer erzeugt wurde (z.B. QtWidget.QMainWindow oder QtWidget.QDialog)

Die Qt-Widgets (wie z.B. QButton, QComboBox, QSpinBox) verfügen einerseits über Methoden, um ihren Zustand
abzufragen (Bsp value() für eine QSpinBox oder currentText() für QComboBox) und senden andererseits
bei Eintreffen bestimmter Ereignisse "Signale" aus, welche mit selbst definierten Methoden ("Slots") 
verbunden werden können (mittels der "connect" Methode). 
Zum Beispiel sendet ein QButton ein "clicked"-Signal aus, wenn er gedrückt wird. Im folgenden Code
wird sie mit der selber definierten "okButtonPressed"-Methode verknüpft.
"""

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('formular.ui', self)
        self.btnOK.clicked.connect(self.okButtonPressed)    # Verknüpfung Signal mit Slot
        self.show()
        
    def okButtonPressed(self):                              # Slot
        anzahl = self.spAnzahl.value()
        art = self.cbArt.currentText()
        print(f"Sie bestellen {anzahl} {art}-Sandwiches")
        txt = self.txtBemerkungen.toPlainText()
        if txt != "":
            print(f"Ihre Bemerkungen: {txt}")

# Instanzierung und Ausführung    
app = QtWidgets.QApplication([])
window = Ui()
app.exec_()
