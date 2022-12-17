nom = input("quel est votre nom ?\n")
age = input("quel est votre age ?\n")
age =int(age)
if age < 12:
    print("bonjour" +nom+ "vous etes mineur !")
elif 12 <= age <18 :
    print(f"Bonjour {nom} vous etes Ado !")
else:
    print("Bonjour" ,nom, "vous etes Adultes !")
    