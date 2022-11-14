import socket
import modulo_tag

class Receiver():
    global sock
    UDP_PORT = 2522
    UDP_IP = ""
    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM,) # UDP
    sock.bind((UDP_IP, UDP_PORT))
    #sock.settimeout(10) #TEMPO DI ATTESA MASSIMO PER DATI

    @staticmethod
    def read():

        while True:

            data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
            data_lista =[]
            for byte in data:
                data_lista.append(byte)
            modulo_tag.elaborate_data(data_lista)
