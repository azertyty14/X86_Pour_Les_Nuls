from instruction.instruction import Instruction
from instruction.i_operande import IOperande

class Mov(Instruction):
    def __init__(self, op_src : IOperande, op_dest : IOperande):
        self.op_src = op_src
        self.op_dest = op_dest
    
    def execute_instruction(self, etat):
        self.op_src.set_value(etat, self.op_dest.get_value(etat))
        
    