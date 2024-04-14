import sys
import personne, vuePersonne, annuaire, vueAnnuaire
from PyQt6.QtWidgets import QApplication, QPushButton

class Controller:
    # constructor
    def __init__(self) -> None:
        # attribut
        self.modele = annuaire.Annuaire('annuaire.json')
        self.vue = vueAnnuaire.VueAnnuaire()
        p = self.modele.getPersonne()
        if isinstance(p, personne.Personne): 
            self.vue.updatePersonne(p)
        
        # slots ie callback
        self.vue.nextClicked.connect(self.next)
        self.vue.previousClicked.connect(self.previous)
        self.vue.openFileClicked.connect(self.openFile)
        self.vue.newClicked.connect(self.new)
        self.vue.personneChanged.connect(self.update)
        self.vue.saveAsClicked.connect(self.saveAs)
        self.vue.vuePersonneInterface.estDecedeCheckBox.stateChanged.connect(self.checkDeath)
        
        
        
    def update(self, d) -> None:
        if d:
            newPersonne = personne.Personne(
                 d["prenom"], d["nom"], d["genre"], d["naissance"], d["mort"], d["bio"], d["est_decede"]
                )
            self.modele.update(newPersonne)
            
            
            
    def checkDeath(self, p) -> None:
        personneD = self.modele.getPersonne()
        self.modele.update(personneD)
        self.vue.updatePersonne(personneD)
        
            
    
    def next(self) -> None:
        self.modele.next()
        next_person = self.modele.getPersonne()
        
        if next_person:
            new_person = personne.Personne(
                next_person.prenom, next_person.nom, next_person.genre, 
                next_person.naissance, next_person.mort, next_person.bio, next_person.est_decede
            )
        self.vue.updatePersonne(new_person)
        self.checkDeath(new_person)
    
    def previous(self) -> None:
        self.modele.previous()
        previous_personne = self.modele.getPersonne()
        
        if previous_personne:
            new_person = personne.Personne(
                previous_personne.prenom, previous_personne.nom, previous_personne.genre, 
                previous_personne.naissance, previous_personne.mort, previous_personne.bio, previous_personne.est_decede
            )
            self.vue.updatePersonne(new_person)
            self.checkDeath(new_person)
    
    def new(self) -> None:
        self.vuePersonneTemp = vuePersonne.VuePersonne()

        self.envoyerButton = QPushButton('Envoyer')
        self.envoyerButton.clicked.connect(self.handleEnvoyer)

        self.vuePersonneTemp.buttonsBottomLayout.addWidget(self.envoyerButton)

        self.vuePersonneTemp.show()
        
    def handleEnvoyer(self):
        d = self.vuePersonneTemp.getAllInfo()
        newPersonne = personne.Personne(
                d["prenom"], d["nom"] , d["genre"], d["naissance"], d["mort"], d["bio"], d["est_decede"]
                )
        
        self.modele.addPersonne(newPersonne)
        self.vuePersonneTemp.close()
        self.checkDeath(newPersonne)
    
    def openFile(self, fname : str) -> None:
        self.modele.open(fname)
        p = self.modele.getPersonne()
        if isinstance(p, personne.Personne): 
            self.vue.updatePersonne(p)
    
    def saveAs(self, fname : str) -> None:
        self.modele.save(fname)
    

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = Controller()
    an = controller.vue.vuePersonneInterface
    an.show()
    sys.exit(app.exec())
