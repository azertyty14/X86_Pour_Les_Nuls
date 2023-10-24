from instruction.instruction import Instruction
from instruction.i_operande import IOperande
from etat.etat_interne import EtatInterne

class Push(Instruction):
    def __init__(self, op : IOperande):
        self.op = op
    
    def execute_instruction(self, etat : EtatInterne):
        etat.set_registre_value("esp", etat.get_registre_value("esp") - 4)
        etat.set_value_from_memory(etat.get_registre_value("esp"), self.op.get_value(etat))
    
    def affiche(self) -> str:
        return "push " + self.op.affiche()
            
    