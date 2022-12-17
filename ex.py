#creation de calculatrice
def addition(x,y):
    return x+y
def soustraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y
print("Bienvenue dans notre calco")

print("1-addition")
print("2-soustraction")
print("3-multiplication")
print("4-division")
choix=int(input("que voulez-vous faire ?"))
if choix==1:
    x= int(input("entrer le premier nombre"))
    y= int(input("entrer le deuxieme nombre"))
    print(addition(x,y))
    
elif choix==2:
    x= int(input("entrer le premier nombre"))
    y= int(input("entrer le deuxieme nombre"))
    print(soustraction(x,y))
    
elif choix==3:
    x= int(input("entrer le premier nombre"))
    y= int(input("entrer le deuxieme nombre"))
    print(multiplication(x,y))
    
elif choix==4:
    x= int(input("entrer le premier nombre"))
    y= int(input("entrer le deuxieme nombre"))
    print(division(x,y))
    
else:
    print("Merci d'avoir utiliser notre calco")