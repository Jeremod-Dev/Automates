from minimisateur import Minimisateur
def main():
    matA = [
        [0,1,0,0,0,0,0],
        [0,0,0,0,0,1,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1],
        [0,0,1,0,0,0,0],
        [0,0,0,0,0,1,0],
        [0,0,0,0,0,1,0]
    ]

    matB = [
        [0,0,0,0,1,0,0],
        [0,0,1,0,0,0,0],
        [0,0,1,0,0,0,0],
        [0,0,0,0,1,0,0],
        [0,0,0,0,0,1,0],
        [0,0,0,1,0,0,0],
        [0,0,1,0,0,0,0]
    ]
    etatFinal = 2
    minimisateur = Minimisateur(matA,matB,etatFinal)
    afficheTab(minimisateur.identique())
    print(len(minimisateur.identique()))
    #print(minimisateur.toutCombinaison([2,3]))

def afficheTab(mat):
    for ligne in mat:
        print(ligne)
    print("\n")


if __name__ == '__main__':
    main()