from instruction.special_instruction.custom_instruction import CustomInstruction
from instruction.i_operande import IOperande
from etat.etat_interne import EtatInterne

## __cdecl
## put an str in pointed(param_1)

class StrCreateInstruction(CustomInstruction):
    def __init__(self, value : str) -> None:
        self.value = value
         
    def execute_instruction(self, etat : EtatInterne):
        param_1 = etat.get_value_from_memory(etat.get_registre_value("esp"))
        print("========== STRCREATE ==========")
        j = etat.get_value_from_memory(param_1)
        for i in self.value:
            etat.set_value_from_memory(param_1, ord(i))
            param_1 += 1
        print(self.value)
        print("========== END STRCREATE ==========")
    
    def affiche(self) -> str:
        return "strcreate"
        
    