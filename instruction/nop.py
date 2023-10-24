from instruction.instruction import Instruction
from instruction.i_operande import IOperande
from etat.etat_interne import EtatInterne

class Nop(Instruction):
    def __init__(self):
        pass
    
    def execute_instruction(self, etat : EtatInterne):
        pass
    
    def affiche(self) -> str:
        return "nop"
        
    