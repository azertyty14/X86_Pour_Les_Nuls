from etat.etat_interne import EtatInterne
from instruction.i_operande import IOperande

class RepereOperande(IOperande):
    def __init__(self, nom : int) -> None:
        self.nom = nom
    
    def get_value(self, etat : EtatInterne) -> int:
        return etat.find_repere(self.nom) + 1
    
    def set_value(self, etat : EtatInterne, valeur : int):
        print("Erreur dans RepereOperande on ne peut pas set la valeur")
    
    def get_address(self, etat: EtatInterne) -> int:
        print("Erreur dans RepereOperande on ne peut pas récuperer d'adresse")
    
    def affiche(self) -> str:
        return "@" + self.nom