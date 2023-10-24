from etat.etat_interne import EtatInterne

class IOperande:
    def get_value(self, etat : EtatInterne) -> int:
        pass
    
    def set_value(self, etat : EtatInterne, valeur : int):
        pass
    
    def get_address(self, etat: EtatInterne) -> int:
        pass

    def affiche(self) -> str:
        pass