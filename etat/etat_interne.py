from instruction.repere import Repere

class EtatInterne:
    def __init__(self, instruction) -> None:
        self.state = {"eax" : 0, "ebx" : 0, "ecx" : 0, "edx" : 0, "eip": 0, "ebp" : 0, "esi" : 0, "edi": 0, "null": 0}
        self.memoire = [0 for _ in range(10001)]
        self.state["esp"] = len(self.memoire) - 1
        self.instruction = instruction
        self.flags = {"CF" : 0, "ZF": 0, "OF": 0, "SF": 0}
        
    def get_registre_value(self, nom : str) -> int:
        return self.state[nom]
    
    def set_registre_value(self, nom : str, val : int):
        self.state[nom] = val
    
    def get_value_from_memory(self, adress : int) -> int:
        return self.memoire[adress]
    
    def set_value_from_memory(self, adress : int, value : int):
        self.memoire[adress] = value

    def get_flag_value(self, flag: str) -> int:
        return self.flags[flag]
    
    def set_flag_value(self, flag: str, value: int):
        self.flags[flag] = value
    
    def find_repere(self, nom) -> int:
        for i in self.instruction:
            if type(i) is Repere:
                if i.nom == nom:
                    return i.addr
        print("Not found Error")
    
    def execute_instruction(self):
        if self.state["eip"] < len(self.instruction):
            print(self.instruction[self.state["eip"]].affiche())
            self.instruction[self.state["eip"]].execute_instruction(self)
            self.state["eip"] += 1
            return True
        else:
            return False
    
    def print_stack(self):
        s = []
        i = 9996
        while i >= self.state["esp"]:
            s.append(self.memoire[i])
            i -= 4
        print("stack",s)
    
    def affiche(self):
        print("state", self.state)
        print("flags", self.flags)
        self.print_stack()
    
    def execute_all(self, interactif = False):
        i = 0
        b = True
        while b:
            print("tour numero: " + str(i))
            b = self.execute_instruction()
            i += 1
            self.affiche()
            print("-----------------------------------------------")
            if interactif:
                input()