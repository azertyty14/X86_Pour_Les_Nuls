from instruction.instruction import Instruction
from instruction.i_operande import IOperande

# TODO + WARNING ! : Flag are not set yet !!!!

class Dec(Instruction):
    def __init__(self, op_dest : IOperande):
        self.op_dest = op_dest
    
    def execute_instruction(self, etat):
        self.op_dest.set_value(etat, self.op_dest.get_value(etat) - 1)
        
    