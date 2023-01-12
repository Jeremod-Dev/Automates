from AFNconvertor import *
from Automate import *

def main():
    afn : Automate = Automate("./automate.txt")
    convertisseur: AFNconvertor = AFNconvertor(afn)

    afd : Automate = convertisseur.afnToAfd()

    print(f"L'AFD produit par l'AFN entrée:\
Nombre etat: {afd.getNbEtat}\
Etats finaux: {afd.getEtatsFinaux}\
Transition A: {afd.getTransitionsA}\
Transition B: {afd.getTransitionsB}")

if __name__ == '__main__':
    main()