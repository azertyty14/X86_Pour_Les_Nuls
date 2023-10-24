from factory.i_instruction_factory import IInstructionFactory
from instruction.instruction import Instruction
from factory.operande_factory import OperandeFactory
from instruction.special import Special
from instruction.nop import Nop
from instruction.special_instruction.pritnf import PrintfInstruction
from instruction.special_instruction.strlen import StrlenInstruction
from instruction.special_instruction.str_create import StrCreateInstruction

class SpecialFactory(IInstructionFactory):
    def get_instruction(line: str) -> Instruction:
        line = line[8:]
        print(line)
        if line == "printf":
            return Special(PrintfInstruction())
        elif line == "strlen":
            return Special(StrlenInstruction())
        elif line[:10] == "str_create":
            return Special(StrCreateInstruction(line[11:]))
        return Special(Nop())
        