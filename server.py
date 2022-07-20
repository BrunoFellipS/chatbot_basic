import socket


class Server:
    def __init__(self):
        self.servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servidor.bind(('localhost', 8888))

        self.servidor.listen()

    def server_action(self):
        cliente, end = self.servidor.accept()

        terminado = False

        while not terminado:
            msg = cliente.recv(1024).decode('utf-8')
            if msg == 'tt':
                terminado = True

            else:
                print(msg)

            cliente.send(input('Mensagem: ').encode('utf-8'))

        cliente.close()
        self.servidor.close()

if __name__ == '__main__':
    s = Server()
    s.server_action()
