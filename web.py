import socket
import time

from config import *
import modulo_tag


class UDPSERVER:
    # Receiver socket
    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM, )  # UDP
    sock.bind(('', WEB_PORT_REC))
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.settimeout(TIMEOUT_REC)

    @classmethod
    def read(cls):
        try:
            data, addr = cls.sock.recvfrom(WEB_BUFFER_SIZE)
        except:
            return "NO_DATA", "NO_IP"
        data_lista = []
        for byte in data:
            data_lista.append(byte)
        return data_lista, addr

    @classmethod
    def send(cls, request):
        cls.sock.sendto(request, ('<broadcast>', WEB_PORT_BROAD))

    @classmethod
    def richiesta(cls):
        cls.send(WEB_SCAN_REQUEST.encode('ascii'))  # MANDO RICHIESTA BROADCAST
        time.sleep(WEB_REQUEST_SLEEP_TIME)  # ASPETTO TEMPO IMPOSTATO
        data, addr = (cls.read())  # LEGGO COSA MI é ARRIVATO
        print(data)
