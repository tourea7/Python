import pyfiglet

liste_matricule = []
liste_nom = []
liste_prenom = []
liste_naissance = []
compte = {}
mot_de_passe = {}


def Inscription():
        print("\nENREGISTREZ - VOUS\n")
        nom = input("Nom: ")
        prenom = input("Prénoms: ")
        print("Date de naissance")
        jj = input("Jour: ")
        mm = input("Mois: ")
        aaaa = input("Année: ")
        mdp = input("Mot de passe: ")
        date_naissance = jj + '/' + mm + '/' + aaaa
        matricule = nom[0:3] + mm + jj
        matricule = matricule.upper()
        liste_matricule.append(matricule)
        liste_nom.append(nom)
        liste_prenom.append(prenom)
        liste_naissance.append(date_naissance)
        mot_de_passe[matricule] = mdp
        compte[matricule] = 36000
        with open('eleve.txt','w') as eleve:
                print('',file=eleve)
                eleve.write(f"Nom : {nom}\n")
                eleve.write(f"Prenoms : {prenom}\n")
                eleve.write(f"Date de naissance : {date_naissance}\n")
                eleve.write(f"Matricule : {matricule}\n")
                eleve.write(f"Solde : {compte}\n")
                print('_'*30, file=eleve)
        print("\nInscription réussie ! \nVous beneficiez d'une bourse de 36000 Fcfa !\n")
        print(f"Matricule: {matricule}")
        print("Utilisez ce matricule et votre mot de passe pour vous connecter à votre compte\n")
       
Inscription()

def afficher():
                eleve = open("eleve.txt",'r')
                print(eleve.read())
                eleve.close()