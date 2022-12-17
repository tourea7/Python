#programmation server
import socket #module pour le reseau

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP
serveur.bind(("192.168.1.2",5000))
serveur.listen(5)
print("serveur en écoute !")
while True:
        client,infoclient=serveur.accept()
        print("connexion etablie avec" +infoclient[0])
        requet=client.recv(255)
        print(requet.decode("utf-8"))
        reponse="Bonjour c'est moi le serveur !"
        client.send(reponse).encode("utf-8")
        client.close()
        serveur.close()