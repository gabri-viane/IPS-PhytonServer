import socket
import time
import random
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
        id = str(random.randint(0, 255)).encode('ascii')
        cls.sock.sendto(request + id, ('<broadcast>', WEB_PORT_BROAD))
        return id

    @classmethod
    def richiesta(cls):
        id = cls.send(WEB_SCAN_REQUEST.encode('ascii'))  # MANDO RICHIESTA BROADCAST
        time.sleep(WEB_REQUEST_SLEEP_TIME)  # ASPETTO TEMPO IMPOSTATO
        while True:
            data, addr = (cls.read())  # LEGGO COSA MI é ARRIVATO

            if data != "NO_DATA" and data[1] == id:  # SE CI SONO DATI E L'ID DELLA RICHIESTA E' UGUALE AGGIUNGILI
                print(data)
                if data[0] == ANTENNA_SEND_TAGS:  # SE LA RISPOSTA E' DELLA SCANSIONE, SALVA I DATI
                    modulo_tag.elaborate_data(data, addr)

            else:  # SE NON CI SON PIU' DATI NEL BUFFER RIMANDA RICHIESTA
                break
