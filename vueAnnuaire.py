# --- import
import json, copy, os, sys
import personne, genre, vuePersonne, datetime, annuaire
from PyQt6.QtCore import pyqtSignal, QDate, Qt
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QFileDialog


# -------------------------------------------------
# --- class Annuaire
# -------------------------------------------------
class VueAnnuaire(QWidget):
    # Signals 
    nextClicked = pyqtSignal()
    previousClicked = pyqtSignal()
    openFileClicked = pyqtSignal(str)
    newClicked = pyqtSignal()
    personneChanged = pyqtSignal(dict)
    saveAsClicked =pyqtSignal(str)
    
    # constructor
    def __init__(self):
        super().__init__()
       
        
        # Create instance
        self.vuePersonneInterface = vuePersonne.VuePersonne()

        # buttons 
        self.ButtonPrevious = QPushButton('<< previous')
        self.ButtonLoad = QPushButton('load')
        self.ButtonNew = QPushButton('new')
        self.ButtonSave = QPushButton('save as')
        self.ButtonNext = QPushButton('next >>')
        
        
        # Add Layout
        self.vuePersonneInterface.buttonsBottomLayout.addWidget(self.ButtonPrevious)
        self.vuePersonneInterface.buttonsBottomLayout.addWidget(self.ButtonLoad)
        self.vuePersonneInterface.buttonsBottomLayout.addWidget(self.ButtonNew)
        self.vuePersonneInterface.buttonsBottomLayout.addWidget(self.ButtonSave)
        self.vuePersonneInterface.buttonsBottomLayout.addWidget(self.ButtonNext)
        
        # signals 
        self.ButtonPrevious.clicked.connect(self.previousClicked.emit)
        self.ButtonLoad.clicked.connect(self.showFileDialogOpen)
        self.ButtonNew.clicked.connect(self.newClicked.emit)
        self.ButtonSave.clicked.connect(self.showFileDialogSave)
        self.ButtonNext.clicked.connect(self.nextClicked.emit)
        
        self.vuePersonneInterface.personneChanged.connect(self.handlePersonneChanged)
            
         
    def handlePersonneChanged(self, info: dict):
        self.personneChanged.emit(info)
        
    def showFileDialogOpen(self):
        filePath, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'JSON Files (*.json);;All Files (*.*)')
        if filePath:
            if not filePath.endswith('.json'):
                filePath += '.json'
            self.openFileClicked.emit(filePath)

        
    def showFileDialogSave(self):
        filePath, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'JSON Files (*.json);;All Files (*.*)')
        if filePath:
            if not filePath.endswith('.json'):
                filePath += '.json'
            self.saveAsClicked.emit(filePath)
            print(filePath)

    def updatePersonne(self, p : personne.Personne):
        self.vuePersonneInterface.updatePersonne(
            p.prenom, p.nom, p.genre, p.naissance, p.mort, p.bio, p.est_decede
            )
        


# --- main: kind of unit test
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    print('TEST: class Annuaire')
    an = VueAnnuaire()
    vue_personne = an.vuePersonneInterface
    vue_personne.show()
    sys.exit(app.exec())

            