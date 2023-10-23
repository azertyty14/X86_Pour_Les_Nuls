from factory.i_instruction_factory import IInstructionFactory
from instruction.instruction import Instruction
from factory.operande_factory import OperandeFactory
from instruction.end import End

class EndFactory(IInstructionFactory):
    def get_instruction(line: str) -> Instruction:
        return End()
        