from instruction.special_instruction.custom_instruction import CustomInstruction
from instruction.i_operande import IOperande
from etat.etat_interne import EtatInterne

## __cdecl
## put in eax len(str(pointed((param_1)))

class StrlenInstruction(CustomInstruction):    
    def execute_instruction(self, etat : EtatInterne):
        param_1 = etat.get_value_from_memory(etat.get_registre_value("esp"))
        print("========== STRLEN ==========")
        s = 0
        while etat.get_value_from_memory(param_1) != 0:
            param_1 += 1
            s += 1
        print("========== END STRLEN ==========")
        etat.set_registre_value("eax", s)
    
    def affiche(self) -> str:
        return "strlen"
        
    