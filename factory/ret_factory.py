from factory.i_instruction_factory import IInstructionFactory
from instruction.instruction import Instruction
from factory.operande_factory import OperandeFactory
from instruction.ret import Ret

class RetFactory(IInstructionFactory):
    def get_instruction(line: str) -> Instruction:
        line = line[4:]
        line = line.replace(' ','')
        if (len(line) == 0):
            op1 = OperandeFactory.get_operande("0x0")
        else:
            op1 = OperandeFactory.get_operande(line)
        return Ret(op1)
        