class Minimisateur:

    def __init__(self, matA, matB, final) -> None:
        self.matA = self.__transposee(matA)
        self.matB = self.__transposee(matB)
        self.etatfinal = final
        self.file = []
        self.__initFile()
        self.posCoupleCourant = 0

    def __initFile(self):
        for i in range(len(self.matA)):
            if (self.etatfinal!=i):
                if self.etatfinal < i:
                    self.file.append([i,self.etatfinal])
                else:
                    self.file.append([self.etatfinal,i])

    def __transposee(self,mat):
        tmp = [0]*len(mat)
        for i in range(len(mat)):
            tmp[i] = [0]*len(mat[0])

        for i in range (len(mat)):
            for j in range (len(mat[0])):
                tmp[j][i]=mat[i][j]
        return tmp

    def identique(self):
        while self.posCoupleCourant!=len(self.file):
            coupleDistingueTemp = self.coupleDistingue(self.file[self.posCoupleCourant])
            if len(coupleDistingueTemp) != 0:
                self.suppDoublons(coupleDistingueTemp)
            self.posCoupleCourant += 1
        
        return self.file


    #############################
    # Fonction qui donne les nouveaux 
    # couples distingués depuis celui entree
    # 
    # ENTREE: Un tuple
    # SORTIE: liste entier de tuple
    #############################
    def coupleDistingue(self, c):
        couplesSortie = []
        coupleTmp = [None,None]
        try:
            coupleTmp[0] = self.indexes(self.matA[c[0]])
            coupleTmp[1] = self.indexes(self.matA[c[1]])
            couplesSortie.extend(self.toutCombinaison(coupleTmp))
        except:
            pass
        coupleTmp = [None,None]
        try:
            coupleTmp[0] = self.indexes(self.matB[c[0]])
            coupleTmp[1] = self.indexes(self.matB[c[1]])
            couplesSortie.extend(self.toutCombinaison(coupleTmp))
        except:
            pass
        return couplesSortie

    #############################
    # Fonction qui realise toutes les 
    # combinaisons possible entre deux listes
    # ENTREE: Un tuple de listes
    # SORTIE: liste entier
    #############################
    def toutCombinaison(self, c):
        sortie = []
        for i in range(len(c[0])):
            for j in range (len(c[1])):
                sortie.append([c[0][i],c[1][j]])
        return sortie

    #############################
    # Fonction qui recupere la position 
    # de tout les "1" d'un liste
    #
    # ENTREE: Une liste d'entier
    # SORTIE: liste entier OU None
    #############################
    def indexes(self,ligne):
        sortie = []
        for i in range(len(ligne)):
            if ligne[i]==1:
                sortie.append(i)
        if(len(sortie)==0):
            return None
        return sortie

    def suppDoublons(self, liste):
        existeDeja = False
        for eListe in liste:
            for eFile in self.file:
                if (((eListe[0]==eFile[0]) and (eListe[1]==eFile[1]))\
                    or ((eListe[1]==eFile[0]) and (eListe[0]==eFile[1]))):
                    existeDeja = True
            if not existeDeja:
                if eListe[0] < eListe[1]:
                    self.file.append([eListe[1],eListe[0]])
                else:
                    self.file.append([eListe[0],eListe[1]])
            existeDeja = False