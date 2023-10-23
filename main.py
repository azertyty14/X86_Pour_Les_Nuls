import my_parser
from etat.etat_interne import EtatInterne

def main():
    inst = my_parser.get_instruction_list("test.txt")
    state = EtatInterne()
    for i in inst:
        i.execute_instruction(state)
        print(state.state)
    


if __name__ == "__main__":
    main()