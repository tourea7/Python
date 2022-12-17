#correction exercice 3
HT=float(input("quel est le montant Hors taxe ?"))
montantTVA=(HT*20)/100 #calcul du montant TVA
montantTTC=HT*montantTVA
print("le montant HT:",HT)
print("TVA 20%:",montantTVA)
print("le montant TTC:",montantTTC)