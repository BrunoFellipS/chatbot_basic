import socket


class Cliente:
    def __init__(self):
        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.cliente.connect(('localhost', 8888))

    def cliente_action(self):
        terminado = False

        print('Digite tt para terminar o caht')

        while not terminado:
            self.cliente.send(input('Mensagem: ').encode('utf-8'))

            msg = self.cliente.recv(1024).decode('utf-8')

            if msg == 'tt':
                terminado = True

            else:
                print(msg)

        self.cliente.close()

if __name__ == '__main__':
    c = Cliente()
    c.cliente_action()
