import my_parser
from etat.etat_interne import EtatInterne
from argparse import ArgumentParser

def main():
    args = get_args()
    inst = my_parser.get_instruction_list(args.file)
    state = EtatInterne(inst)
    state.execute_all(args.it)
    

def get_args():
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", help="nom du fichier", required=True)
    parser.add_argument("-i", "--it", help="Mode pas à pas", action="store_true")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main()