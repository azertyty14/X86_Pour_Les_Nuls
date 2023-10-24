from instruction.instruction import Instruction
from instruction.i_operande import IOperande
from etat.etat_interne import EtatInterne

class Ret(Instruction):
    def __init__(self, op : IOperande):
        self.op = op
    
    def execute_instruction(self, etat : EtatInterne):
        tmp = etat.get_value_from_memory(etat.get_registre_value("esp"))
        etat.set_registre_value("esp", etat.get_registre_value("esp") + 4)
        etat.set_registre_value("esp", etat.get_registre_value("esp") + self.op.get_value(etat))
        etat.set_registre_value("eip", tmp - 1)

    def affiche(self) -> str:
        return "ret " + self.op.affiche()