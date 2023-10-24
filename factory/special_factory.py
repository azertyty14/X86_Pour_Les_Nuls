from factory.i_instruction_factory import IInstructionFactory
from instruction.instruction import Instruction
from factory.operande_factory import OperandeFactory
from instruction.special import Special
from instruction.nop import Nop
from instruction.special_instruction.pritnf import PrintfInstruction

class SpecialFactory(IInstructionFactory):
    def get_instruction(line: str) -> Instruction:
        line = line[8:]
        print(line)
        if line == "printf":
            return Special(PrintfInstruction())
        return Special(Nop())
        