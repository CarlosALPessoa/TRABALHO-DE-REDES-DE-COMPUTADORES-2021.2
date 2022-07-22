import socket 
import threading

meu_ip='localhost'
minha_porta= 8000


#SERVER = socket.gethostbyname(socket.gethostname())
my_server= (meu_ip, 8000)
FORMATO = 'utf-8'

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind(my_server)
desx = "DESCONECTADO!"

def execut(cons, addr_doclient, atv):
	print(f"[NOVA CONEXÃO] {addr_doclient} connectado.")
	while atv:
			msg_recebida = cons.recv(65).decode(FORMATO)
			if msg_recebida:
				msg_recebida = int(msg_recebida)
				msg = cons.recv(msg_recebida).decode(FORMATO)
				if msg == desx:
					atv = False
					print(f"Cliente: {addr_doclient} foi desconectado")
				else:	
					print(f"Recebido: {msg}  ; Do cliente: {addr_doclient}")
	cons.close()
    

def start():
	#server.listen()
	tcp.listen()
	print(f"[LISTANDO] TCP é listado em {my_server}")
	servidor = True
	while True:
		#conn, addr = server.accept()
		conn, addr_doclient = tcp.accept()
		#	print("O cliente = ", doclient, "se conectou")

		thread = threading.Thread(target=execut, args=(conn, addr_doclient, 'TRUE'))
		thread.start()
		print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        
print("[INICIALIZANDO] Servidor está iniciando...")
start()
