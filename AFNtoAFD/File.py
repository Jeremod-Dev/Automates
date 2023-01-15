from Etat import *
from SuperEtat import *

class File:
    
    def __init__(self) -> None:
        self.__supEtats: list[SuperEtat] = []
        self.__iterateur : int = 0

    def ajouterEtat(self, supEtat: SuperEtat)->None:
        self.__supEtats.append(supEtat)

    def incrementerIterateur(self)-> None:
        self.__iterateur += 1
    
    def resetIterateur(self)-> None:
        self.__iterateur = 0

    def existe(self, nomSupEtat: list[int])-> bool:
        for itSupEtat in self.__supEtats:
            if itSupEtat.getNom() == nomSupEtat:
                return True
        return False
    
    def estAuBout(self) -> bool:
        return self.__iterateur == len(self.__supEtats)

    def getEtatCourant(self)-> SuperEtat:
        return self.__supEtats[self.__iterateur]

    def getTete(self)-> SuperEtat:
        return self.__supEtats[len(self.__supEtats)-1]