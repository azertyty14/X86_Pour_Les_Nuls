from instruction.instruction import Instruction

class Repere(Instruction):
    def __init__(self, nom : str, addr : int):
        self.nom = nom
        self.addr = addr
    
    def execute_instruction(self, etat):
        pass
    
    def affiche(self) -> str:
        return "@" + self.nom
        
    