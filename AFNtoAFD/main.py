from AFNconvertor import *
from AFN import *
from AFD import *

def main():
    afn : AFN = AFN()
    afn.chargerAutomateFichier(".\\AFNtoAFD\\automate.txt")
    convertisseur: AFNconvertor = AFNconvertor(afn)

    afd : AFD = convertisseur.afnToAfd()

    print(f"L'AFD produit par l'AFN entrée:\
Nombre etat: {afd.getNbEtat()}\
Etats finaux: {afd.getEtatsFinaux}\
Nom etats ordonnés: {afd.getEtats()}\
Transition A: {afd.getTransitionsA()}\
Transition B: {afd.getTransitionsB()}")

if __name__ == '__main__':
    main()