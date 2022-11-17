from datetime import datetime
import pandas as pd
from time import perf_counter


class TAG:
    def __init__(self, codice):
        self.codice = codice
        self.dati = {}

    def add_value(self, antenna, value, tempo):
        if tempo in self.dati:
            self.dati[tempo][antenna] = value
        else:
            self.dati[tempo] = {antenna: value}

    def dataframe(self):
        df = pd.DataFrame.from_dict(self.dati, orient="index")
        return df


class TAGS:
    lista = []

    @classmethod
    def add_tag(cls, tag_n):  # AGGIUNGO UN TAG
        cls.lista.append(TAG(tag_n))

    @classmethod
    def search_tag(cls, codice):  # CERCO SE IL TAG ESISTE GIA"
        for i in range(len(cls.lista)):
            if cls.lista[i].codice == codice:
                return i
        return "NON PRESENTE"

    @classmethod
    def add_value(cls, codice, value, antenna, tempo):
        codice = str(codice)
        value = int(value)
        antenna = int(antenna)

        index = TAGS.search_tag(codice)

        if not isinstance(index, int):
            TAGS.add_tag(codice)
            index = TAGS.search_tag(codice)
        cls.lista[index].add_value(antenna, value, tempo)

    @classmethod
    def dataframe(cls):
        for tag in cls.lista:
            print(tag.dati)
            print(tag.dataframe())


def elaborate_data(data, addr):
    tempo = datetime.now().strftime('%H:%M:%S')
    richiesta = data[0]
    id_antenna = data[1]
    n_tag = int(data[2])
    lista_tag = data[3::]
    i = 0
    while i < len(lista_tag):
        elab_tag = lista_tag[:6]
        mac = ':'.join(elab_tag)
        rssi = lista_tag[6]
        lista_tag = lista_tag[7:]

        TAGS.add_value(mac, rssi, id_antenna, tempo)
        i += 1
