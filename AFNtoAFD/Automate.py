class Automate:
    
    def __init__(self,path:str)->None:
        self.__transitionsA : list[list[int]] = []
        self.__transitionsB : list[list[int]] = []
        self.__etatsfinaux: list[int] = []
        self.__nbEtat: int = 0
        self.__chargerAutomate(path)
        self.__transitionsA = self.__transposee(self.__transitionsA)
        self.__transitionsB = self.__transposee(self.__transitionsB)

    #############################
    # méthode qui charge les données de l'automate
    #
    # ENTREE: chaine de caractere
    # SORTIE: RIEN
    #############################
    def __chargerAutomate(self, path:str)->None:
        stdin = self.__ouvrirFichier(path)
        self.__nbEtat = int(stdin[0][0])
        self.__etatsfinaux = [int(i) for i in stdin[1]]
        for i in range(2,self.__nbEtat+2):
            self.__transitionsA.append([int(j) for j in stdin[i]])
        for i in range(self.__nbEtat+2,self.__nbEtat*2+2):
            self.__transitionsB.append([int(j) for j in stdin[i]])
        if self.__nbEtat > 10:
            raise ValueError("L'automate est trop grand")

    #############################
    # méthode qui ouvrir le fichier avec l'automate,
    # qui scinde chaque caractere et supprime \n
    #
    # ENTREE: chaine de caractere
    # SORTIE: Liste 
    #############################
    def __ouvrirFichier(self,path: str):
        #TODO methode d'ouverture de fichier qui renvoie les données de l'automate
        sortie :list[str]= []
        with open(path, "r") as fichier:
            for line in fichier.readlines():
                line = line.replace("\n","")
                ligne = line.split(" ")
                sortie.append(ligne)
        return sortie

    #############################
    # Fonction qui realise la 
    # transposée d'une matrice
    #
    # ENTREE: matrice
    # SORTIE: matrice
    #############################
    def __transposee(self,mat):
        tmp = [0]*len(mat)
        for i in range(len(mat)):
            tmp[i] = [0]*len(mat[0])

        for i in range (len(mat)):
            for j in range (len(mat[0])):
                tmp[j][i]=mat[i][j]
        return tmp

    def getTransitionsA(self)-> list[list[int]]:
        return self.__transitionsA

    def getTransitionsB(self)-> list[list[int]]:
        return self.__transitionsB

    def getEtatsFinaux(self)->list[int]:
        return self.__etatsfinaux

    def getNbEtat(self)->int:
        return self.__nbEtat