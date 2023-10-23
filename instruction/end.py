from instruction.instruction import Instruction
from instruction.i_operande import IOperande
from etat.etat_interne import EtatInterne

class End(Instruction):
    def __init__(self):
        pass
    
    def execute_instruction(self, etat : EtatInterne):
        etat.set_registre_value("eip", len(etat.instruction))
    
    def affiche(self) -> str:
        return "end"
        
    