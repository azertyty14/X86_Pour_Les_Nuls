from etat.etat_interne import EtatInterne
from instruction.i_operande import IOperande

class SimpleOperande(IOperande):
    def __init__(self, nom : str) -> None:
        self.nom = nom
    
    def get_value(self, etat : EtatInterne) -> int:
        return etat.get_registre_value(self.nom)
    
    def set_value(self, etat : EtatInterne, valeur : int):
        etat.set_registre_value(self.nom, valeur)