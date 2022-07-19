import socket


class Servidor:
    def __init__(self):
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor.bind('localhost', 8888)
