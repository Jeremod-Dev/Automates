from AFN import *
from AFD import *
from File import *
from SuperEtat import *

class AFNconvertor:
    def __init__(self, afn : AFN) -> None:
        self.__afn : AFN = afn
        self.__fileA : File = File()
        self.__fileB : File = File()

    def afnToAfd(self)-> AFN:
        etatInit : Etat = self.__afn.getEtats()[0]
        self.__fileA.ajouterEtat(SuperEtat([etatInit.getNom()],etatInit.getEstTerminal()))
        self.__fileA.getTete().setTransitionA(self.__afn.getTransitionsA()[etatInit.getNom()])
        while not self.__fileA.estAuBout():
            transitions : list[int] = self.__recupTransitionADepuisEtat(self.__fileA.getEtatCourant())
            nomSuperEtat = self.__indexes(transitions)
            estTerminal = self.__unDesEtatsEstTerminal(nomSuperEtat)
            if not (self.__fileA.existe(nomSuperEtat)): # si le nom etat existe pas dans la file
                self.__fileA.ajouterEtat(SuperEtat(nomSuperEtat,estTerminal))
                self.__fileA.getTete().setTransitionA(transitions)
            
            self.__fileA.incrementerIterateur()
        self.__fileA.resetIterateur()
        print("ed")

    def __unDesEtatsEstTerminal(self, nomSupEtat : list[int])->bool:
        #TODO Boucle sur les etats du superEtat et renvoyer vrai si au moins un est terminal
        for etat in self.__afn.getEtats():
            for nomEtat in nomSupEtat:
                if etat.getNom()==nomEtat and etat.getEstTerminal():
                    return True
        return False

    def __recupTransitionADepuisEtat(self, supEtat : SuperEtat) -> list[int]:
        transitions : list[list[int]] = []
        transitionsSorti : list[int] = []
        if len(supEtat.getNom())==1:
            return self.__afn.getTransitionsA()[supEtat.getNom()[0]]
        for etat in supEtat.getNom():
            transitions.append(self.__afn.getTransitionsA()[supEtat.getNom()[etat]])
        transitionsSorti = transitions[0]
        for i in range (len(transitions)-1):
            transitionsSorti = self.__ou(transitionsSorti,transitions[i+1])
        return transitionsSorti
        
    def __recupTransitionBDepuisEtat(self, supEtat : SuperEtat) -> list[int]:
        transitions : list[list[int]] = []
        transitionsSorti : list[int] = []
        if len(supEtat.getNom())==1:
            return self.__afn.getTransitionsB()[supEtat.getNom()[0]]
        for etat in supEtat.getNom():
            transitions.append(self.__afn.getTransitionsB()[supEtat.getNom()[etat]])
        transitionsSorti = transitions[0]
        for i in range (len(transitions)-1):
            transitionsSorti = self.__ou(transitionsSorti,transitions[i+1])
        return transitionsSorti

    def __ou(self, l1 : list[int], l2: list[int])->list[int]:
        sortie: list[int] = []
        for it in range (0,len(l1)):
            if l1[it]==0 and l2[it]==0:
                sortie.append(0)
            else:
                sortie.append(1)
        return sortie
    

    #############################
    # Fonction qui recupere la position 
    # de tous les "1" d'une liste
    #
    # ENTREE: liste transition de l'etat de depart
    # SORTIE: liste entier des etats arrives
    #############################
    def __indexes(self, etatPointe: list[int]) -> list[int]:
        sortie :list[int] = []
        for transition in range(self.__afn.getNbEtat()):
            if etatPointe[transition]==1:
                sortie.append(transition)
        if(len(sortie)==0):
            return None
        return sortie