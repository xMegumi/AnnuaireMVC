# --- import
import json, copy, os
import personne, genre, datetime
from PyQt6.QtCore import QObject, pyqtSignal

# -------------------------------------------------
# --- class Annuaire
# -------------------------------------------------
class Annuaire:
    # constructor
    def __init__(self, jsonFile : (str|None) = None) -> None:
        # attributs
        self.__listPersonne : list[personne.Personne] = []
        self.__current : (int|None) = None
        
        # si un fichier est fourni : on charge 
        if jsonFile: self.open(jsonFile)

    @property
    def current(self) -> int | None : return self.__current
    @current.setter
    def current(self, index :int|None) -> None : self.__current = index

    def update(self,p: personne.Personne) -> None:
        pp = self.getPersonne()
        if pp:
            pp.genre = copy.deepcopy(p.genre)
            pp.prenom = copy.deepcopy(p.prenom)
            pp.nom = copy.deepcopy(p.nom)
            pp.naissance = copy.deepcopy(p.naissance)
            pp.mort = copy.deepcopy(p.mort) 
            pp.bio = copy.deepcopy(p.bio)
            pp.est_decede = copy.deepcopy(p.est_decede)


    def open(self, jsonFile: str) -> None:
        self.__listPersonne = []
        self.__current = 0
        with open(jsonFile, encoding='utf-8') as file:
            print(f'Loading file: {jsonFile}', end='... ')
            js = json.load(file) 
            if 'annuaire' in js.keys():
                annuaire_data = js['annuaire']
                added_person_count = 0

                for person_data in annuaire_data:
                    new_person = personne.Personne.buildFromJSon(person_data)

                    # Vérification que la date de décès est supérieure ou égale à la date de naissance
                    if new_person.mort and new_person.mort < new_person.naissance:
                        print(f"\nERROR: La date de décès de {new_person.prenom} {new_person.nom} est antérieure à sa date de naissance.\nLa personne n'a pas été chargée.")
                    else:
                        # Vérification si la personne existe déjà dans l'annuaire
                        is_duplicate = any(existing_person == new_person for existing_person in self.__listPersonne)
                        if not is_duplicate:
                            self.__listPersonne.append(new_person)
                            added_person_count += 1

                print(f'{added_person_count} new person(s) added.')
                self.__current = 0 if self.__listPersonne else None


    def save(self,jsonFile : str) -> None:
        print(f'saving file: {jsonFile}', end='... ')

        if not  os.path.exists(jsonFile): 
            f = open(jsonFile, "x"); f.close()

        with open(jsonFile, "w", encoding='utf-8') as file: 
            d : dict= {} 
            listPersonne : list= []
            for p in self.__listPersonne :listPersonne.append(json.loads(p.toJSON()))
            d['annuaire'] = listPersonne
            json.dump(d,file,ensure_ascii=False)
        print(f'done!')



    def getPersonneByName(self, name: str) -> (personne.Personne|None):
        searchList : list[str] = list(map(lambda x: x.nom.lower(), self.__listPersonne))
        return self.__listPersonne[searchList.index(name.lower())]

    def addPersonne(self, p : personne.Personne, index : int|None = None) -> None :
        is_duplicate = any(existing_person == p for existing_person in self.__listPersonne)
    
        if not is_duplicate:
            if p.mort == datetime.date and p.mort < p.naissance:
                print(f"ERROR: La date de décès de {p.prenom} {p.nom} est antérieure à sa date de naissance.")
            else:
                if not isinstance(index, int) or not isinstance(self.__current, int):
                    self.__listPersonne.append(p)
                    self.current = len(self.__listPersonne) - 1 if len(self.__listPersonne) != 0 else None
                else:
                    self.__listPersonne.insert(self.__current, p)
        else:
            print("ERROR: Personne identique déjà présente dans l'annuaire.")
            
    def next(self) -> None :
        if self.__current != None :
            self.__current = (self.__current +1)% len(self.__listPersonne) 
    
    def previous(self) -> None :
        if self.__current != None :
            self.__current = (self.__current - 1)% len(self.__listPersonne)

    def getPersonne(self) -> personne.Personne| None : 
        if self.__current != None: return self.__listPersonne[self.__current]  
        else: return None

