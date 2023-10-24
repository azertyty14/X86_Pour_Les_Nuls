from instruction.instruction import Instruction
from instruction.special_instruction.custom_instruction import CustomInstruction
from instruction.i_operande import IOperande
from etat.etat_interne import EtatInterne

class Special(Instruction):
    def __init__(self, custom: CustomInstruction):
        self.custom = custom
    
    def execute_instruction(self, etat : EtatInterne):
        self.custom.execute_instruction(etat)
    
    def affiche(self) -> str:
        return "special"
        
    