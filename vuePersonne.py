import datetime
import genre as g
from PyQt6.QtCore import pyqtSignal, QDate, Qt
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QComboBox, QLineEdit, QDateEdit, QTextEdit, QLabel, QCheckBox
import sys

# ----------------------------------------------------
# --- class VuePersonne
# ----------------------------------------------------
class VuePersonne(QWidget):
    personneChanged: pyqtSignal = pyqtSignal(dict)
    
    def __init__(self):
        super().__init__()

        self.mainLayout = QVBoxLayout(self)
        self.personTopLayout = QHBoxLayout()
        self.personBottomLayout = QHBoxLayout()
        self.buttonsBottomLayout = QHBoxLayout()
        self.personBottomLayoutLabel1 = QHBoxLayout()
        self.personBottomLayoutLabel2 = QHBoxLayout()
        
        self.genre = QComboBox()
        self.genre.addItems(["M. ", "Mme ", "_ "])
        self.prenom = QLineEdit("Prénom")
        self.nom = QLineEdit("Nom")
        self.labelNais = QLabel('Né le : ')
        self.dateNaissance = QDateEdit()
        self.dateNaissance.setDateRange(QDate(1, 1, 1), QDate.currentDate())
        self.labelMort = QLabel('Mort le : ')
        self.dateMort = QDateEdit() 
        self.dateMort.setDateRange(QDate(1, 1, 1), QDate.currentDate())
        self.bio = QTextEdit('"biographie"')
        self.estDecedeCheckBox = QCheckBox("Est décédé")

        self.mainLayout.addLayout(self.personTopLayout)
        self.mainLayout.addSpacing(10)
        self.mainLayout.addLayout(self.personBottomLayout)
        self.mainLayout.addStretch()
        self.mainLayout.addWidget(self.bio)
        self.mainLayout.addStretch()
        self.mainLayout.addLayout(self.buttonsBottomLayout)
        
        self.personTopLayout.addWidget(self.genre)
        self.personTopLayout.addWidget(self.prenom)
        self.personTopLayout.addWidget(self.nom)
        
        self.personBottomLayout.addLayout(self.personBottomLayoutLabel1)
        self.personBottomLayout.addStretch()
        self.personBottomLayout.addLayout(self.personBottomLayoutLabel2)

        self.personBottomLayoutLabel1.addWidget(self.labelNais)
        self.personBottomLayoutLabel1.addWidget(self.dateNaissance)
        self.personBottomLayoutLabel2.addWidget(self.labelMort)
        self.personBottomLayoutLabel2.addWidget(self.dateMort)

        self.personBottomLayoutLabel1.setAlignment(self.labelNais, Qt.AlignmentFlag.AlignRight)
        self.personBottomLayoutLabel1.setAlignment(self.dateNaissance, Qt.AlignmentFlag.AlignLeft)
        self.personBottomLayoutLabel2.setAlignment(self.labelMort, Qt.AlignmentFlag.AlignRight)
        self.personBottomLayoutLabel2.setAlignment(self.dateMort, Qt.AlignmentFlag.AlignLeft)

        self.buttonsBottomLayout.addWidget(self.estDecedeCheckBox)

        self.genre.currentIndexChanged.connect(self.emitSignal)
        self.prenom.editingFinished.connect(self.emitSignal)
        self.nom.editingFinished.connect(self.emitSignal)
        self.bio.textChanged.connect(self.emitSignal)
        self.dateNaissance.dateChanged.connect(self.emitSignal)
        self.dateMort.dateChanged.connect(self.emitSignal)
        self.estDecedeCheckBox.stateChanged.connect(self.toggleMortFieldsVisibility) 
        
        if self.estDecedeCheckBox.isChecked() == False:
            self.labelMort.hide()
            self.dateMort.hide()
        else:
            self.labelMort.show()
            self.dateMort.show()
            

    def emitSignal(self):
        info = self.getAllInfo()
        self.personneChanged.emit(info)
    
    def getAllInfo(self): 
        genre = self.genre.currentText()
        if genre == 'M' or genre == 'M. ':
            genreOut = g.Genre.M
        elif genre == 'Mme ' or genre == 'F':
            genreOut = g.Genre.F
        elif genre == '_ ':
            genreOut = g.Genre.O
        
        date_naissance = self.dateNaissance.date()
        naissance = datetime.date(date_naissance.year(), date_naissance.month(), date_naissance.day())
        
        mort = ""
        if self.estDecedeCheckBox.isChecked():
            date_mort = self.dateMort.date()
            mort = datetime.date(date_mort.year(), date_mort.month(), date_mort.day())

        est_decede = self.estDecedeCheckBox.isChecked()

        info = {
            "genre": genreOut,
            "prenom": self.prenom.text(),
            "nom": self.nom.text(),
            "naissance": naissance,
            "mort": mort,
            "bio": self.bio.toPlainText(),
            "est_decede": est_decede
        }
        return info
        
    def updatePersonne(self, prenom: str, nom: str, genre: g.Genre,
               nee: datetime.date, mort: datetime.date | None,
               bio: str, est_decede: bool): 
        if genre == g.Genre.M:
            self.genre.setCurrentIndex(0)  
        elif genre == g.Genre.F:
            self.genre.setCurrentIndex(1)  
        elif genre == g.Genre.O:
            self.genre.setCurrentIndex(2)
        self.prenom.setText(prenom)
        self.nom.setText(nom)
        self.dateNaissance.setDate(QDate(nee))

        # Vérifie si la personne est décédée ou non
        if est_decede:
            self.estDecedeCheckBox.setChecked(True)
            self.labelMort.show()
            self.dateMort.show()
            # Si une date de décès est fournie, l'afficher
            if mort:
                self.dateMort.setDate(QDate(mort))
            else:
                # Sinon, vider la date de décès
                self.dateMort.setDate(QDate.currentDate())
        else:
            self.estDecedeCheckBox.setChecked(False)
            self.labelMort.hide()
            self.dateMort.hide()
        self.bio.setText(bio)



    def toggleMortFieldsVisibility(self, state):
        if state == self.estDecedeCheckBox.isChecked():
            self.labelMort.hide()
            self.dateMort.hide()
        else:
            self.dateMort.setDate(QDate.currentDate())
            self.labelMort.show()
            self.dateMort.show()
        self.emitSignal()

        

        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    vue = VuePersonne()
    vue.show()
    sys.exit(app.exec())
