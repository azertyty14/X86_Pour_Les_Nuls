from etat.etat_interne import EtatInterne
from instruction.i_operande import IOperande

class ConstOperande(IOperande):
    def __init__(self, value : int) -> None:
        self.value = value
    
    def get_value(self, etat : EtatInterne) -> int:
        return self.value
    
    def set_value(self, etat : EtatInterne, valeur : int):
        print("Erreur dans ConstOperande on ne peut pas set la valeur")
    
    def get_address(self, etat: EtatInterne) -> int:
        print("Erreur dans ConstOperande on ne peut pas récuperer d'adresse")
    
    def affiche(self) -> str:
        return hex(self.value)