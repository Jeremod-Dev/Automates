from AFNconvertor import *
from AFN import *

def main():
    afn : AFN = AFN()
    #afn.chargerAutomateFichier(".\\AFNtoAFD\\automate.txt")
    afn.chargerAutomateFichier("./automate.txt")
    convertisseur: AFNconvertor = AFNconvertor(afn)
    print(convertisseur)

if __name__ == '__main__':
    main()