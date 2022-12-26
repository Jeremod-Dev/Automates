from minimiseur import *
from Automate import *

def main():
    automate : Automate = Automate("Minimisation/automate.txt")
    minimiseur :Minimiseur = Minimiseur(automate)

    print(f"Les états identiques de l'automate sont: {minimiseur.etatsIdentique()}")
    print(f"L'automate minimiser fait {minimiseur.nbEtatMinimise()}")


if __name__ == '__main__':
    main()