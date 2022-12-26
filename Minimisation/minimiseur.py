from File import *
from Automate import *

class Minimiseur:

    def __init__(self, automate: Automate) -> None:
        self.__file: File = File()
        self.__automate : Automate = automate
        self.__etatsIndistingable: list[int] = []
        self.__initFile()

    #############################
    # Fonction qui recherche les couples
    # identiques
    #
    # ENTREE: RIEN
    # SORTIE: Liste de couple
    #############################
    def etatsIdentique(self):
        while not self.__file.estAuBout():
            coupleDistingueTemp = self.__coupleDistingue(self.__file.getCoupleCourant())
            if len(coupleDistingueTemp) != 0:
                self.enregistrerCouples(coupleDistingueTemp)
            self.__file.incrementerIterateur()
        
        for couple in self.__couplesManquants():
            for etat in couple:
                if not (etat in self.__etatsIndistingable):
                    self.__etatsIndistingable.append(etat)

        return self.__etatsIndistingable

    #############################
    # Fonction qui renvoi le nombre d'etat
    # de l'automate minimiser
    # 
    # ENTREE: RIEN
    # SORTIE: Entier
    #############################
    def nbEtatMinimise(self)-> int:
        return self.__automate.getNbEtat()-len(self.__etatsIndistingable)+1

    #############################
    # Fonction qui donne les nouveaux 
    # couples distingués depuis celui entree
    # 
    # ENTREE: Un tuple
    # SORTIE: liste entier de tuple
    #############################
    def __coupleDistingue(self, l_etats) -> list[list[int]]:
        couplesSortie :list[list[int]] = []
        coupleTmp : list[int] = [None,None]
        try:
            premierEtat :int = l_etats[0]
            secondEtat :int = l_etats[1]

            coupleTmp[0] = self.__indexes(self.__automate.getTransitionsA()[premierEtat])
            coupleTmp[1] = self.__indexes(self.__automate.getTransitionsA()[secondEtat])
            couplesSortie.extend(self.__toutesCombinaisons(coupleTmp))
        except: 
            pass  # Déclenché si absence de transition pour ce symbole pour l'etat
        coupleTmp = [None,None]
        try:
            coupleTmp[0] = self.__indexes(self.__automate.getTransitionsB()[premierEtat])
            coupleTmp[1] = self.__indexes(self.__automate.getTransitionsB()[secondEtat])
            couplesSortie.extend(self.__toutesCombinaisons(coupleTmp))
        except:
            pass  # Déclenché si absence de transition pour ce symbole pour l'etat
        return couplesSortie

    #############################
    # Fonction qui recupere la position 
    # de tous les "1" d'un liste
    #
    # ENTREE: liste transition de l'etat de départ
    # SORTIE: liste entier des états arrivés
    #############################
    def __indexes(self, etatPointe: list[int]) -> list[int]:
        sortie :list[int] = []
        for transition in range(self.__automate.getNbEtat()):
            if etatPointe[transition]==1:
                sortie.append(transition)
        if(len(sortie)==0):
            return None
        return sortie

    #############################
    # Fonction qui realise toutes les 
    # combinaisons possible entre deux listes
    # ENTREE: Un tuple de listes
    # SORTIE: liste entier
    #############################
    def __toutesCombinaisons(self, l_couple: list[list[int]])->list[list[int]]:
        sortie :list[list[int]] = []
        for i in range(len(l_couple[0])):
            for j in range (len(l_couple[1])):
                sortie.append([l_couple[0][i],l_couple[1][j]])
        return sortie

    #############################
    # Fonction qui initialise la file
    # avec des etats triviaux (final / non final)
    # ENTREE: Un tuple de listes
    # SORTIE: liste entier
    #############################
    def __initFile(self)->None:
        for etatFinal in self.__automate.getEtatsFinaux():
            for i in range(self.__automate.getNbEtat()):
                if (etatFinal!=i):
                    if etatFinal < i:
                        self.__file.ajouterCouple([i,etatFinal])
                    else:
                        self.__file.ajouterCouple([etatFinal,i])

    #############################
    # Fonction qui renvoi les couples qui sont
    # manquant dans la file
    #
    # ENTREE: RIEN
    # SORTIE: Une liste des couples d'etat
    #############################
    def __couplesManquants(self)-> list[list[int]]:
        etats : list[list[int]]= []
        for premier in range (0,self.__automate.getNbEtat()):
            for second in range (0,self.__automate.getNbEtat()):
                if not ([premier,second] in etats) and not([second,premier] in etats):
                    if premier >= second :
                        etats.append([premier,second])
                    else:
                        etats.append([second,premier])
            self.__file.ajouterCouple([premier,premier])
        for coupleATester in self.__file.getCouples():
            try:
                etats.remove(coupleATester)
            except:
                pass
            try:
                etats.remove([coupleATester[1],coupleATester[0]])
            except:
                pass
        return etats

    #############################
    # Fonction qui supprime les tuples
    # qui existe deja dans la file
    #
    # ENTREE: Une liste d'entier
    # SORTIE: RIEN
    #############################
    def enregistrerCouples(self, liste)->None:
        for coupleATester in liste:
            if not self.__file.coupleExiste(coupleATester):
                if coupleATester[0] < coupleATester[1]:
                    self.__file.ajouterCouple([coupleATester[1],coupleATester[0]])
                else:
                    self.__file.ajouterCouple([coupleATester[0],coupleATester[1]])