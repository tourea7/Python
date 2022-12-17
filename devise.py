#Devise
import pyfiglet


pub=pyfiglet.figlet_format("D E V I S E")
print(pub)
#creation de Fonction
def dollar():
        montant=input("Entrez le montant: ")
        try:
                montant=float(montant)
        except:
                print("Le montant est invalide!")
        else:
                valeur= montant*0.99
                print(montant, "Euro =", valeur, "Dollar")
def fcfa():
        montant=input("Entrez le montant: ")
        try:
                montant=float(montant)
        except:
                print("Le montant est invalide !")
        else:
                valeur= montant*655.77
                print(montant, "Euro =", valeur, "Fcfa")
print()
print("CONVERTISSEUR EURO EN DOLLAR OU FCFA")
while True:
        print("-"*50)
        print()
        print("choissisez le type de conversion \n")
        print("1- Euro en Dollars")
        print("2- Euro en FCFA")
        choix = input("--> ")
        try:
            choix = int(choix)
        except:
            print("ERREUR!, choix incorrect")
        else:
            if choix == 1:
                dollar()
            elif choix == 2:
                fcfa()
            else:
                print("ERREUR!, choix incorrect")

