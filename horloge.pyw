#importer les modules 
from tkinter import * 
from tkinter.ttk import *
 #importer la fonction strftime dans récupérer l'heure du système
from time import strftime
  
#création d'une fenêtre tkinter
root = Tk()
root.title('Horloge')
root.geometry("600x400")
  
# Creer une fonction pour afficher l'heure sur l'interface
def horloge():
    heure = strftime('%H:%M:%S')
    ladate= strftime('%b %d %Y')
    lbl.config(text = heure)
    lbl.after(1000, horloge)
    lbl2.config(text=ladate)
  
#Rendre l'horloge plus attrayant
lbl = Label(root, font = ('Courier', 40, 'bold'),
            background = 'Black',
            foreground = 'white')
lbl.pack(pady=20)

lbl2 = Label(root, font=('Helvetica', 14))
lbl2.pack(pady=10)

  

horloge()
  
mainloop()