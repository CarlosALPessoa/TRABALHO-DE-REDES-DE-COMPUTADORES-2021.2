import socket
from threading import Thread

SERVER = 'localhost'
PORTA = 8000
FORMATO = 'utf-8'
descx = "DESCONECTADO!"

destino = (SERVER, PORTA)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(destino)

def send(msg):
    escrito = msg.encode(FORMATO)
    msg_length = len(escrito)
    send_length = str(msg_length).encode(FORMATO)
    send_length += b' ' * (65 - len(send_length))
    client.send(send_length)
    client.send(escrito)

while True:
    print("Digite uma mensagem: ")
    msg = input()
    send(msg)
    if msg == descx:
        print("Desconectado ao servidor.")
        break
