from instruction.instruction import Instruction
from instruction.i_operande import IOperande

# TODO + WARNING ! : All Flag are not set yet !!!! And not sure for flag

class Cmp(Instruction):
    def __init__(self, op_1 : IOperande, op_2 : IOperande):
        self.op_1 = op_1
        self.op_2 = op_2
    
    def execute_instruction(self, etat):
        temp = self.op_1.get_value(etat) - self.op_2.get_value(etat)
        if temp < 0:
            etat.set_flag_value("CF", 1)
            etat.set_flag_value("SF", 1)
            etat.set_flag_value("OF", 1)
        else:
            etat.set_flag_value("CF", 0)
            etat.set_flag_value("SF", 0)
            etat.set_flag_value("OF", 0)
        if temp == 0:
            etat.set_flag_value("ZF", 1)
        else:
            etat.set_flag_value("CF", 0)
        
    def affiche(self) -> str:
        return "cmp " + self.op_1.affiche() + ", " + self.op_2.affiche()
            
            
        
    