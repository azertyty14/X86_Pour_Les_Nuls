from factory.i_instruction_factory import IInstructionFactory
from instruction.instruction import Instruction
from factory.operande_factory import OperandeFactory
from instruction.lea import Lea

class LeaFactory(IInstructionFactory):
    def get_instruction(line: str) -> Instruction:
        line = line[4:]
        line = line.replace(' ','')
        line = line.split(',')
        op1 = OperandeFactory.get_operande(line[0])
        op2 = OperandeFactory.get_operande(line[1])
        return Lea(op1, op2)
        