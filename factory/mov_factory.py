from factory.i_instruction_factory import IInstructionFactory
from instruction.instruction import Instruction
from factory.operande_factory import OperandeFactory
from instruction.mov import Mov

class MovFactory(IInstructionFactory):
    def get_instruction(line: str) -> Instruction:
        line = line.replace(',', '')
        line = line.split(' ')
        op1 = OperandeFactory.get_operande(line[1])
        op2 = OperandeFactory.get_operande(line[2])
        return Mov(op1, op2)
        