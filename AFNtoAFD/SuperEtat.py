from Etat import *
class SuperEtat(Etat):

    def __init__(self, nom: list[int], estTerminal : bool) -> None:
        self.__nom : list[int] = nom
        self.__estTerminal : bool = estTerminal
        self.__transitionA : list[int] = []
        self.__transitionB : list[int] = []
    
    def setTransitionA(self, transition : list[int])-> None:
        self.__transitionA = transition

    def setTransitionB(self, transition : list[int])-> None:
        self.__transitionB = transition

    def getNom(self)-> list[int]:
        return self.__nom

    def getEstTerminal(self)-> bool:
        return self.__estTerminal

    def getTransitionA(self)-> list[int]:
        return self.__transitionA

    def getTransitionB(self)-> list[int]:
        return self.__transitionB