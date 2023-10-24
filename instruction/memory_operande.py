from etat.etat_interne import EtatInterne
from instruction.i_operande import IOperande

class MemoryOperande(IOperande):
    def __init__(self, reg1: str, reg2 : str, scale: int, offset : int):
        self.reg1 = reg1
        self.reg2 = reg2
        self.scale = scale
        self.offset = offset
        
    def get_address(self, etat: EtatInterne) -> int:
        return etat.get_registre_value(self.reg1) + etat.get_registre_value(self.reg2) * self.scale + self.offset

    def get_value(self, etat: EtatInterne) -> int:
        return etat.get_value_from_memory(self.get_address(etat))
    
    def set_value(self, etat: EtatInterne, valeur: int):
        etat.set_value_from_memory(self.get_address(etat), valeur)
    
    def affiche(self) -> str:
        return "[" + self.reg1 + "+" + self.reg2 + "*" + hex(self.scale) + "+" + hex(self.offset) + "]"