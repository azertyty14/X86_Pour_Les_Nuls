import my_parser
from etat.etat_interne import EtatInterne

def main():
    inst = my_parser.get_instruction_list("test.txt")
    state = EtatInterne(inst)
    while state.execute_instruction():
        print(state.state)
    


if __name__ == "__main__":
    main()