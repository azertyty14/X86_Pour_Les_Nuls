from instruction.instruction import Instruction
from instruction.i_operande import IOperande
from etat.etat_interne import EtatInterne

# TODO + WARNING ! : Flag are not set yet !!!!
# TODO + WARNING ! : Only in EAX no EDX

class Mul(Instruction):
    def __init__(self, op : IOperande):
        self.op = op
    
    def execute_instruction(self, etat : EtatInterne):
        etat.set_registre_value("eax", etat.get_registre_value("eax")*self.op.get_value(etat))
    
    def affiche(self) -> str:
        return "mul " + self.op.affiche()
        
    