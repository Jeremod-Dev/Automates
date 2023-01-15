class Etat:

    def __init__(self, nom : int, estTerminal : bool) -> None:
        self.__nom = nom
        self.__estTerminal = estTerminal

    def getNom(self)->int:
        return self.__nom
    
    def getEstTerminal(self)->bool:
        return self.__estTerminal