import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.1.2",5000))  # pour se connecter au serveur d'adresse ip renseignée
print("Connexion établie !")
while True:
    txt=input('Vous: ')
    client.send(txt.encode("utf-8"))
    reponse = client.recv(255).decode("utf-8")
    print('Tya:',reponse)
    client.close()