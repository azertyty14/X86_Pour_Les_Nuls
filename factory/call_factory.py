from factory.i_instruction_factory import IInstructionFactory
from instruction.instruction import Instruction
from factory.operande_factory import OperandeFactory
from instruction.call import Call

class CallFactory(IInstructionFactory):
    def get_instruction(line: str) -> Instruction:
        line = line[5:]
        line = line.replace(' ','')
        op1 = OperandeFactory.get_operande(line)
        return Call(op1)
        