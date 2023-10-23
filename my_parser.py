from instruction.instruction import Instruction
from factory.mov_factory import MovFactory
from factory.lea_factory import LeaFactory
from factory.mul_factory import MulFactory
from factory.add_factory import AddFactory
from factory.sub_factory import SubFactory
from factory.inc_factory import IncFactory
from factory.dec_factory import DecFactory
from factory.jmp_factory import JmpFactory
from factory.pop_factory import PopFactory
from factory.push_factory import PushFactory
from factory.call_factory import CallFactory
from factory.ret_factory import RetFactory
from factory.end_factory import EndFactory
from factory.nop_factory import NopFactory
from instruction.repere import Repere

def get_lines(filename: str):
    with open(filename, "r") as f:
        data = f.read()
    return data.split("\n") 

def get_instruction_list(filename : str):
    inst = get_lines(filename)
    instruction_list = []
    i = 0
    for l in inst:
        a = l.split(' ')
        if a[0] == "mov":
            instruction_list.append(MovFactory.get_instruction(l))
        elif a[0] == "lea":
            instruction_list.append(LeaFactory.get_instruction(l))
        elif a[0] == "add":
            instruction_list.append(AddFactory.get_instruction(l))
        elif a[0] == "sub":
            instruction_list.append(SubFactory.get_instruction(l))
        elif a[0] == "mul":
            instruction_list.append(MulFactory.get_instruction(l))
        elif a[0] == "inc":
            instruction_list.append(IncFactory.get_instruction(l))
        elif a[0] == "dec":
            instruction_list.append(DecFactory.get_instruction(l))
        elif a[0] == "jmp":
            instruction_list.append(JmpFactory.get_instruction(l))
        elif a[0] == "pop":
            instruction_list.append(PopFactory.get_instruction(l))
        elif a[0] == "push":
            instruction_list.append(PushFactory.get_instruction(l))
        elif a[0] == "call":
            instruction_list.append(CallFactory.get_instruction(l))
        elif a[0] == "ret":
            instruction_list.append(RetFactory.get_instruction(l))
        elif a[0] == "end":
            instruction_list.append(EndFactory.get_instruction(l))
        elif len(a[0]) > 0 and a[0][0] == "@":
            instruction_list.append(Repere(a[0][1:], i))
        else:
            print("instruction inconnu")
            instruction_list.append(NopFactory.get_instruction(l))
        i += 1
    return instruction_list