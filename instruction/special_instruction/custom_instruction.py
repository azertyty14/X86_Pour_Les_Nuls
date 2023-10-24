from instruction.instruction import Instruction
from instruction.i_operande import IOperande
from etat.etat_interne import EtatInterne

class CustomInstruction(Instruction):    
    def execute_instruction(self, etat : EtatInterne):
        pass
        
    