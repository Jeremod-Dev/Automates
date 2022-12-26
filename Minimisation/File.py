class File:
    
    def __init__(self) -> None:
        self.__couples: list[list[int]] = []
        self.__iterateur : int = 0

    def ajouterCouple(self, couples: list[list[int]])->None:
        self.__couples.append(couples)

    def coupleExiste(self, c_aTester: list[int])->bool:
        if c_aTester in self.__couples:
            return True
        return False

    def getCouples(self)-> list[list[int]]:
        return self.__couples

    def incrementerIterateur(self)-> None:
        self.__iterateur += 1
    
    def estAuBout(self) -> bool:
        return self.__iterateur == len(self.__couples)

    def getCoupleCourant(self)-> list[int]:
        return self.__couples[self.__iterateur]