from instruction.instruction import Instruction
from factory.mov_factory import MovFactory

def get_lines(filename: str):
    with open(filename, "r") as f:
        data = f.read()
    return data.split("\n") 

def get_instruction_list(filename : str):
    inst = get_lines(filename)
    instruction_list = []
    for l in inst:
        a = l.split(' ')
        if a[0] == "mov":
            instruction_list.append(MovFactory.get_instruction(l))
        else:
            print("instruction inconnu")
    return instruction_list