from factory.i_instruction_factory import IInstructionFactory
from instruction.instruction import Instruction
from factory.operande_factory import OperandeFactory
from instruction.push import Push

class PushFactory(IInstructionFactory):
    def get_instruction(line: str) -> Instruction:
        line = line[5:]
        line = line.replace(' ','')
        op1 = OperandeFactory.get_operande(line)
        return Push(op1)
        