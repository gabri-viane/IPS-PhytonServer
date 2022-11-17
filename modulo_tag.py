from datetime import datetime


class TAG:
    def __init__(self, codice):
        self.codice = codice
        self.antenne = []

    # aggiungo una lista in caso una nuova antenna sia riconosciuta
    # abbiamo quindi potenzialmente infinite antenne
    def add_antenna(self, antenna, valore):
        self.antenne.append({"n_antenna": antenna,
                             "valori": {self.orario(): valore}})

    # aggiungo valore
    def add_value(self, antenna, valore):
        index = self.search_dict(antenna)
        if isinstance(index, int):
            self.antenne[index]["valori"][self.orario()] = valore
        else:
            self.add_antenna(antenna, valore)

    # cerco se e' stata gia' creata antenna
    def search_dict(self, antenna):
        for i in range(len(self.antenne)):
            if antenna == self.antenne[i]["n_antenna"]:
                return i
        return "NON_PRESENTE"

    def print_antenne(self):
        print(f"\nNUMERO TAG:{self.codice}")
        print(f"ANTENNE CREATE: {len(self.antenne)}")
        for antenna in self.antenne:
            print(f"NUMERO ANTENNA: {antenna['n_antenna']}")
            print(antenna["valori"])
        print("\n")

    def orario(self):
        return datetime.now().strftime('%H:%M:%S')


class TAGS:
    global lista
    lista = []

    @staticmethod
    def add_tag(tag_n):  # AGGIUNGO UN TAG
        lista.append(TAG(tag_n))

    @staticmethod
    def search_tag(codice):  # CERCO SE IL TAG ESISTE GIA"
        for i in range(len(lista)):
            if lista[i].codice == codice:
                return i
        return "NON PRESENTE"

    @staticmethod
    def add_value(codice, value, antenna):
        codice = int(codice)
        value = int(value)
        antenna = int(antenna)

        index = TAGS.search_tag(codice)

        if not isinstance(index, int):
            TAGS.add_tag(codice)
            index = TAGS.search_tag(codice)

        lista[index].add_value(antenna, value)
        TAGS.print_tags()

    @staticmethod
    def print_tags():
        for tag in lista:
            tag.print_antenne()


def elaborate_data(data, addr):#DA SISTEMARE
    id_antenna = data[0]
    n_tag = int(data[1])
    lista_tag = data[2::]
    i = 0
    while i < len(lista_tag):
        TAGS.add_value(lista_tag[i], lista_tag[i + 1], id_antenna)
        i += 2
