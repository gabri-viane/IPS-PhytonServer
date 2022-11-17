import configparser
import os.path

config = configparser.ConfigParser()

# Crea file di configurazione se non esiste
if not os.path.isfile("config.ini"):
    print("""
    FILE DI CONFIGURAZIONE NON TROVATO.
    CREO IL FILE DI CONFIGURAZIONE CON I VALORI DI DEFAULT.""")
    config['WEB'] = {
        'PORT_REC': 2522,
        'PORT_BROAD': 2523,
        'TIMEOUT_REC': 3,
        'REQUEST_SLEEP_TIME': 2,
        'SCAN_REQUEST': 221,
        'SYNC_REQUEST': 220,
        'DEEP_SLEEP_REQUEST': 254,
        'STOP_REQUEST': 255,
        'BUFFER_SIZE': 1024,
        'ANTENNA_SEND_INFO': 200,
        'ANTENNA_SEND_BUFFER_DISCONNECTED': 202,
        'ANTENNA_SEND_TAGS': 203
    }
    with open("config.ini", 'w') as configfile:
        config.write(configfile)

# Salviamo tutta la configurazione in una variabile locale.
# Andremo a prendere da qui le nostre variabili
config.read('config.ini')
WEB_PORT_REC = int(config['WEB']['PORT_REC'])
TIMEOUT_REC = int(config['WEB']['TIMEOUT_REC'])
WEB_PORT_BROAD = int(config['WEB']['PORT_BROAD'])
WEB_REQUEST_SLEEP_TIME = int(config['WEB']['REQUEST_SLEEP_TIME'])
WEB_SCAN_REQUEST = str(config['WEB']['SCAN_REQUEST'])
WEB_SYNC_REQUEST = str(config['WEB']['SYNC_REQUEST'])
WEB_DEEP_SLEEP_REQUEST = str(config['WEB']['DEEP_SLEEP_REQUEST'])
WEB_STOP_REQUEST = str(config['WEB']['STOP_REQUEST'])
WEB_BUFFER_SIZE = int(config['WEB']['BUFFER_SIZE'])
ANTENNA_SEND_INFO = str(config['WEB']['ANTENNA_SEND_INFO'])
ANTENNA_SEND_BUFFER_DISCONNECTED = str(config['WEB']['ANTENNA_SEND_BUFFER_DISCONNECTED'])
ANTENNA_SEND_TAGS = str(config['WEB']['ANTENNA_SEND_TAGS'])
