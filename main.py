import my_parser
from etat.etat_interne import EtatInterne

def main():
    inst = my_parser.get_instruction_list("factoriel.txt")
    state = EtatInterne(inst)
    j = 0
    while state.execute_instruction() and j < 1000:
        state.affiche()
        j += 1
    


if __name__ == "__main__":
    main()