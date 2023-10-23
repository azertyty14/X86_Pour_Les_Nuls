from instruction.instruction import Instruction
from instruction.i_operande import IOperande

# TODO + WARNING ! : Flag are not set yet !!!!

class Add(Instruction):
    def __init__(self, op_dest : IOperande, op_src : IOperande):
        self.op_dest = op_dest
        self.op_src = op_src
    
    def execute_instruction(self, etat):
        self.op_dest.set_value(etat, self.op_dest.get_value(etat) + self.op_src.get_value(etat))
        
    