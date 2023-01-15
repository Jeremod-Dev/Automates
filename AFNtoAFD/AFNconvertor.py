from AFN import *
from File import *
from Etat import *
from SuperEtat import *

class AFNconvertor:
    def __init__(self, afn : AFN) -> None:
        self.__afn : AFN = afn
        self.__file : File = File()
        self.__transitionA: list[list[int]] = []
        self.__transitionB: list[list[int]] = []
        self.__afnToAfd()

    #############################
    # Fonction qui converti un AFN
    # en AFD
    #
    # ENTREE: superEtat
    # SORTIE: liste entier (0 ou 1)
    #############################
    def __afnToAfd(self)->None:
        self.__initialiserFile()
        self.__rechercheSuperEtat()
        self.__constructionDesTransitions()

    #############################
    # Fonction qui permet de transformer les transitions 
    # d'etats en transition de super etats
    #
    # ENTREE: XXX
    # SORTIE: XXX
    #############################
    def __constructionDesTransitions(self)->None:
        for etatDepart in self.__file.getEtats():
            ligne : list[int] = [0 for _ in range (len(self.__file.getEtats()))]
            ligne[self.__trouverIndexSuperEtatParNom(self.__indexes(etatDepart.getTransitionA()))] = 1
            self.__transitionA.append(ligne)
        for etatDepart in self.__file.getEtats():
            ligne : list[int] = [0 for _ in range (len(self.__file.getEtats()))]
            ligne[self.__trouverIndexSuperEtatParNom(self.__indexes(etatDepart.getTransitionB()))] = 1
            self.__transitionB.append(ligne)

    #############################
    # Fonction qui permet de trouver la position d'un
    # super etat en file grace à son nom
    #
    # ENTREE: nom du super etat recherche
    # SORTIE: entier (position en file)
    #############################
    def __trouverIndexSuperEtatParNom(self,nomRef:list[int])->int:
        for i in range (0, len(self.__file.getEtats())):
            etatActuel = self.__file.getEtats()[i]
            if etatActuel.getNom()==nomRef:
                return i
        return -1

    #############################
    # Fonction qui recherche les supers Etats et qui 
    # les ajoutes en file s'il n'existe pas sinon
    # il modifie les transitions
    #
    # ENTREE: XXX
    # SORTIE: XXX
    #############################
    def __rechercheSuperEtat(self)->None:
        while not self.__file.estAuBout():
            transitionsA : list[int] = self.__recupTransitionADepuisEtat(self.__file.getEtatCourant())
            transitionsB : list[int] = self.__recupTransitionBDepuisEtat(self.__file.getEtatCourant())
            nomSuperEtatA = self.__indexes(transitionsA)
            nomSuperEtatB = self.__indexes(transitionsB)
            estTerminalA = self.__unDesEtatsEstTerminal(nomSuperEtatA)
            estTerminalB = self.__unDesEtatsEstTerminal(nomSuperEtatB)
            if not (self.__file.existe(nomSuperEtatA)): # si le nom etat existe pas dans la file
                self.__file.ajouterEtat(SuperEtat(nomSuperEtatA,estTerminalA))
                self.__file.getTete().setTransitionA(transitionsA)
                self.__file.getTete().setTransitionA(transitionsB)
            else:
                self.__file.getEtatCourant().setTransitionA(transitionsA)
                self.__file.getEtatCourant().setTransitionB(transitionsB)
            if not (self.__file.existe(nomSuperEtatB)): # si le nom etat existe pas dans la file
                self.__file.ajouterEtat(SuperEtat(nomSuperEtatB,estTerminalB))
                self.__file.getTete().setTransitionA(transitionsA)
                self.__file.getTete().setTransitionA(transitionsB)
            else:
                self.__file.getEtatCourant().setTransitionA(transitionsA)
                self.__file.getEtatCourant().setTransitionB(transitionsB)

            self.__file.incrementerIterateur()
        self.__file.resetIterateur()

    #############################
    # Fonction qui permet d'initialiser la file pour commencer 
    # le processus de transformation
    #
    # ENTREE: XXX
    # SORTIE: XXX
    #############################
    def __initialiserFile(self)->None:
        etatInit : Etat = self.__afn.getEtats()[0]
        self.__file.ajouterEtat(SuperEtat([etatInit.getNom()],etatInit.getEstTerminal()))
        self.__file.getTete().setTransitionA(self.__afn.getTransitionsA()[etatInit.getNom()])
        self.__file.getTete().setTransitionB(self.__afn.getTransitionsB()[etatInit.getNom()])

    #############################
    # Fonction qui renvoie vrai si le superEtat est 
    # un etat terminal
    #
    # ENTREE: liste d'entier (nom du superEtat)
    # SORTIE: booleen
    #############################
    def __unDesEtatsEstTerminal(self, nomSupEtat : list[int])->bool:
        #TODO Boucle sur les etats du superEtat et renvoyer vrai si au moins un est terminal
        for etat in self.__afn.getEtats():
            for nomEtat in nomSupEtat:
                if etat.getNom()==nomEtat and etat.getEstTerminal():
                    return True
        return False

    #############################
    # Fonction qui genere la transition de la lettre A d'un super
    # etat en faisant une 'fusion' des états qui le compose
    #
    # ENTREE: superEtat
    # SORTIE: liste entier (0 ou 1)
    #############################
    def __recupTransitionADepuisEtat(self, supEtat : SuperEtat) -> list[int]:
        transitions : list[list[int]] = []
        transitionsSorti : list[int] = []
        if len(supEtat.getNom())==1:
            return self.__afn.getTransitionsA()[supEtat.getNom()[0]]
        for etat in supEtat.getNom():
            transitions.append(self.__afn.getTransitionsA()[etat])
        transitionsSorti = transitions[0]
        for i in range (len(transitions)-1):
            transitionsSorti = self.__ou(transitionsSorti,transitions[i+1])
        return transitionsSorti
        
    #############################
    # Fonction qui genere la transition de la lettre B d'un super
    # etat en faisant une 'fusion' des états qui le compose
    #
    # ENTREE: superEtat
    # SORTIE: liste entier (0 ou 1)
    #############################
    def __recupTransitionBDepuisEtat(self, supEtat : SuperEtat) -> list[int]:
        transitions : list[list[int]] = []
        transitionsSorti : list[int] = []
        if len(supEtat.getNom())==1:
            return self.__afn.getTransitionsB()[supEtat.getNom()[0]]
        for etat in supEtat.getNom():
            transitions.append(self.__afn.getTransitionsB()[etat])
        transitionsSorti = transitions[0]
        for i in range (len(transitions)-1):
            transitionsSorti = self.__ou(transitionsSorti,transitions[i+1])
        return transitionsSorti

    #############################
    # Fonction qui effectue l'operation OU
    # sur des indices d'une liste
    #
    # ENTREE: 2 listes d'entier (0 ou 1)
    # SORTIE: liste entier (0 ou 1)
    #############################
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

    #############################
    # Fonction qui affiche l'objet 
    #
    # Precondition: avoir appelé la methode de conversion
    # ENTREE: XXX
    # SORTIE: chaine de caracteres
    #############################
    def __str__(self) -> str:
        sortie : str = ""
        sortie += "Transition A:\n"
        sortie += 12*" "
        for etat in self.__file.getEtats():
            espace = 10-len(etat.getNom())*3
            sortie += f"|{etat.getNom()}{espace*' '}"
        sortie +="\n==="+len(self.__file.getEtats())*14*"="+"\n"
        j = 0
        for etat in self.__file.getEtats():
            if etat.getEstTerminal():
                sortie +=f"{etat.getNom()}{(10-len(etat.getNom())*3)*' '} *|"
            else:
                sortie +=f"{etat.getNom()}{(10-len(etat.getNom())*3)*' '}  |"
            for i in self.__transitionA[j]:
                sortie +=f"{i}{9*' '}|"
            sortie += "\n"
            j+=1

        sortie += "\n\nTransition B:\n"
        sortie += 12*" "
        for etat in self.__file.getEtats():
            espace = 10-len(etat.getNom())*3
            sortie += f"|{etat.getNom()}{espace*' '}"
        sortie +="\n==="+len(self.__file.getEtats())*14*"="+"\n"
        j = 0
        for etat in self.__file.getEtats():
            if etat.getEstTerminal():
                sortie +=f"{etat.getNom()}{(10-len(etat.getNom())*3)*' '} *|"
            else:
                sortie +=f"{etat.getNom()}{(10-len(etat.getNom())*3)*' '}  |"
            for i in self.__transitionB[j]:
                sortie +=f"{i}{9*' '}|"
            sortie += "\n"
            j+=1
        return sortie