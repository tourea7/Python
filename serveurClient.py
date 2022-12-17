import socket
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.1.2",5000))
print("Connexion établie !")
reponse=client.recv(255).decode("utf-8")
print(reponse)
rp=input(">>")
client.send(rp.encode("utf-8"))
client.close()