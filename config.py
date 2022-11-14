import configparser
import os.path

config = configparser.ConfigParser()

# Crea file di configurazione se non esiste
if not os.path.isfile("config.ini"):
    config['WEB'] = {
        'PORT': 2522,
        'BUFFER_SIZE': 1024}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

# Salviamo tutta la configurazione in una variabile locale.
# Andremo a prendere da qui le nostre variabili
config.read('config.ini')
WEB_PORT = int(config['WEB']['PORT'])
WEB_BUFFER_SIZE = int(config['WEB']['BUFFER_SIZE'])
