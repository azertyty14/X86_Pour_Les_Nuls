from instruction.instruction import Instruction
from instruction.i_operande import IOperande
from etat.etat_interne import EtatInterne

class Call(Instruction):
    def __init__(self, op : IOperande):
        self.op = op
    
    def execute_instruction(self, etat : EtatInterne):
        etat.set_value_from_memory(etat.get_registre_value("esp"), etat.get_registre_value("eip") + 1)
        etat.set_registre_value("esp", etat.get_registre_value("esp") - 4)
        etat.set_registre_value("eip", self.op.get_value(etat) - 1)
    
    def affiche(self) -> str:
        return "call "
            
    