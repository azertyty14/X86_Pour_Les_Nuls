from factory.i_instruction_factory import IInstructionFactory
from instruction.instruction import Instruction
from factory.operande_factory import OperandeFactory
from instruction.pop import Pop

class PopFactory(IInstructionFactory):
    def get_instruction(line: str) -> Instruction:
        line = line[4:]
        line = line.replace(' ','')
        op1 = OperandeFactory.get_operande(line)
        return Pop(op1)
        