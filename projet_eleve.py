from tkinter import*
import pyfiglet

liste_matricule = []
liste_nom = []
liste_prenom = []
liste_naissance = []
compte = {}
mot_de_passe = {}

#Creer une premiere fenetre (fenetre principale)
pub=pyfiglet.figlet_format("MA BANQUE ETUDIANTE")

def Inscription():
        global window1
        window1= Tk()
        window1.title("ENREGISTREZ - VOUS")
        window1.geometry("1080x720")
        window1.minsize(480, 360)
        window1.config(background='#F8F8FF')
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
        print("\nInscription réussie ! \nVous beneficiez d'une bourse de 36000 Fcfa !\n")
        print(f"Matricule: {matricule}")
        print("Utilisez ce matricule et votre mot de passe pour vous connecter à votre compte\n")

Inscription()