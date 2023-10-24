from instruction.instruction import Instruction
from instruction.i_operande import IOperande
from etat.etat_interne import EtatInterne

class Jmp(Instruction):
    def __init__(self, op : IOperande):
        self.op = op
    
    def execute_instruction(self, etat : EtatInterne):
        etat.set_registre_value("eip", self.op.get_value(etat) - 1)
    
    def affiche(self) -> str:
        return "jmp " + self.op.affiche()
        
    