from Etat import *
class AFD:
    
    def __init__(self)->None:
        self.__transitionsA : list[list[int]] = []
        self.__transitionsB : list[list[int]] = []
        self.__etats : list[Etat] = []
        self.__nbEtat: int = 0

    #############################
    # méthode qui charge les données de l'automate
    # depuis les données en parametre
    #
    # ENTREE: entier, liste entier, liste d'entier bidimensionnelle, liste d'entier bidimensionnelle
    # SORTIE: RIEN
    #############################
    def chargerAFD(self, nbEtat: int,etats:list[Etat], transA: list[list[int]],transB: list[list[int]])->None:
        if self.__nbEtat > 10:
            raise ValueError("L'automate est trop grand")
        self.__nbEtat = nbEtat
        self.__etats = etats
        self.__transitionsA = transA
        self.__transitionsB = transB

    def getTransitionsA(self)-> list[list[int]]:
        return self.__transitionsA

    def getTransitionsB(self)-> list[list[int]]:
        return self.__transitionsB

    def getNbEtat(self)->int:
        return self.__nbEtat

    def getEtats(self)->list[Etat]:
        return self.__etats


    def setTransitionsA(self, transA: list[list[int]])->None:
        self.__transitionsA = transA

    def setTransitionsB(self, transB: list[list[int]])->None:
        self.__transitionsB = transB

    def setEtats(self, etats: list[Etat])->None:
        if len(etats)>10:
            raise ValueError("L'automate est trop grand")
        self.__etats = etats
        self.__nbEtat = len(etats)