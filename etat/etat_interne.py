class EtatInterne:
    def __init__(self) -> None:
        self.state = {"eax" : 0, "ebx" : 0, "ecx" : 0, "edx" : 0, "null": 0}
        self.memoire = [0 for _ in range(10001)]
        self.state["esp"] = len(self.memoire) - 1
        
    def get_registre_value(self, nom : str) -> int:
        return self.state[nom]
    
    def set_registre_value(self, nom : str, val : int):
        self.state[nom] = val
    
    def get_value_from_memory(self, adress : int) -> int:
        return self.memoire[adress]
    
    def set_value_from_memory(self, adress : int, value : int):
        self.memoire[adress] = value