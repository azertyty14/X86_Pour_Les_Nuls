from instruction.instruction import Instruction
from instruction.i_operande import IOperande
from etat.etat_interne import EtatInterne

class Jbe(Instruction):
    def __init__(self, op : IOperande):
        self.op = op
    
    def execute_instruction(self, etat : EtatInterne):
        if (etat.get_flag_value("CF") == 1 or etat.get_flag_value("ZF") == 1):
            etat.set_registre_value("eip", self.op.get_value(etat) - 1)
    
    def affiche(self) -> str:
        return "jbe " + self.op.affiche()
        
    