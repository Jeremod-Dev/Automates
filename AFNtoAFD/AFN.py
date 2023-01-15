from Etat import *
from SuperEtat import *
class AFN:
    
    def __init__(self)->None:
        self.__transitionsA : list[list[int]] = []
        self.__transitionsB : list[list[int]] = []
        self.__etats : list[Etat] = []
        self.__nbEtat: int = 0

    #############################
    # méthode qui charge les données de l'automate
    # depuis un fichier texte
    #
    # ENTREE: chaine de caractere
    # SORTIE: RIEN
    #############################
    def chargerAutomateFichier(self, path:str)->None:
        stdin = self.__ouvrirFichier(path)
        self.__nbEtat = int(stdin[0][0])
        if self.__nbEtat > 10:
            raise ValueError("L'automate est trop grand")
        etatsfinaux = [int(i) for i in stdin[1]]
        for i in range(2,self.__nbEtat+2):
            self.__transitionsA.append([int(j) for j in stdin[i]])
        for i in range(self.__nbEtat+2,self.__nbEtat*2+2):
            self.__transitionsB.append([int(j) for j in stdin[i]])
        for i in range(self.__nbEtat):
            self.__etats.append(Etat(i, True if (i in etatsfinaux) else False))

    #############################
    # méthode qui charge les données de l'automate
    # depuis les données en parametre
    #
    # ENTREE: entier, liste entier, liste d'entier bidimensionnelle, liste d'entier bidimensionnelle
    # SORTIE: RIEN
    #############################
    def chargerAutomateAttributs(self, nbEtat: int, etatFinaux: list[int], etats: list[int], transA: list[list[int]],transB: list[list[int]])->None:
        if self.__nbEtat > 10:
            raise ValueError("L'automate est trop grand")
        self.__nbEtat = nbEtat
        self.__etatsfinaux = etatFinaux
        self.__etats = etats
        self.__transitionsA = transA
        self.__transitionsB = transB

    #############################
    # méthode qui ouvrir le fichier avec l'automate,
    # qui scinde chaque caractere et supprime \n
    #
    # ENTREE: chaine de caractere
    # SORTIE: Liste 
    #############################
    def __ouvrirFichier(self,path: str):
        sortie :list[str]= []
        with open(path, "r") as fichier:
            for line in fichier.readlines():
                line = line.replace("\n","")
                ligne = line.split(" ")
                sortie.append(ligne)
        return sortie

    
    def getTransitionsA(self)-> list[list[int]]:
        return self.__transitionsA

    def getTransitionsB(self)-> list[list[int]]:
        return self.__transitionsB

    def getNbEtat(self)->int:
        return self.__nbEtat

    def getEtats(self)->list[int]:
        return self.__etats
