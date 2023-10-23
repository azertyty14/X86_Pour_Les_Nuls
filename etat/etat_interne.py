class EtatInterne:
    def __init__(self) -> None:
        self.state = {"eax" : 0, "ebx" : 0, "ecx" : 0, "edx" : 0}
        
    def get_registre_value(self, nom : str) -> int:
        return self.state[nom]
    
    def set_registre_value(self, nom : str, val : int):
        self.state[nom] = val