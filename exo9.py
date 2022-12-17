#Banque
#creation de dictionnaire
from pydoc import cli
import pyfiglet

pub=pyfiglet.figlet_format("N Y S - B A N K")
print(pub)
comptes={"paul":154.74,"Marie":418.48,"Jean":96.20,"Pauline":914.24}
#creation des fonctions
def depot(client): #fonction 
        montant=float(input("Quel est le montant voulez-vous deposer ? \n"))
        comptes[client]+=montant
        print("Depot effectué !")
def retrait(client):
        montant=float(input("Quel est le montant voulez-vous retirer ? \n"))
        if montant<=comptes[client]:
                comptes[client]-=montant
                print("Retrait effectué !")
        else:
                print("Retrait impossible, verifiez votre solde")
print("Akwaaba à NYS-BANK")
print("-"*50)
for client,solde in comptes.items():
        print(client,":", str(solde))
print("Choisissez une opération: ")
print("D- Dépot")
print("R- Retrait")
print("Q- Quitter")

while True:
        choix=input("Que voulez-vous faire ?")
        if choix=="D":
                client=input("Sur quel compte voulez-vous faire l'operation ?")
                depot(client)
        elif choix=="R":
                client=input("Sur quel compte voulez-vous faire l'operation ?")
                retrait(client)
        elif choix=="Q":
                print("Merci d'etre passé à NYS-BANK")
        else:
                print("Faite un choix !")       