from factory.i_instruction_factory import IInstructionFactory
from instruction.instruction import Instruction
from factory.operande_factory import OperandeFactory
from instruction.nop import Nop

class NopFactory(IInstructionFactory):
    def get_instruction(line: str) -> Instruction:
        return Nop()
        