from instruction.special_instruction.custom_instruction import CustomInstruction
from instruction.i_operande import IOperande
from etat.etat_interne import EtatInterne

## __cdecl
## Si param_1 == 0 : print val(param_2)
## Si param_2 == 1 : print val(pointed(param_2))
## Si param_3 == 2 : print(str(pointed(param_2)))

class PrintfInstruction(CustomInstruction):    
    def execute_instruction(self, etat : EtatInterne):
        param_1 = etat.get_value_from_memory(etat.get_registre_value("esp"))
        param_2 = etat.get_value_from_memory(etat.get_registre_value("esp") + 4)
        print("========== PRINTF ==========")
        if param_1 == 0:
            print(param_2)
        elif param_1 == 1:
            print(etat.get_value_from_memory(param_2))
        elif param_1 == 2:
            j = etat.get_value_from_memory(param_2)
            while j != 0:
                print(chr(j), end="")
                param_2 += 1
                j = etat.get_value_from_memory(param_2)
            print("\n", end="")
        else:
            print("Erreur dans printf")
        print("========== END PRINTF ==========")
    
    def affiche(self) -> str:
        return "printf"
        
    