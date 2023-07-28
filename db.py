from pymongo import MongoClient

client = MongoClient('mongodb+srv://mmps:mariamarta@emisoras.msic7it.mongodb.net/')
db = client['Emisoras']
collectionAM = db['AM']
collectionFM = db['FM']
collectionMundial = db['Mundo']
collectionMusica = db['Libre']

def obtener_AM():
    return collectionAM.find()

def obtener_AM_por_id(emisora_id):
    return collectionAM.find_one({'id': emisora_id})

def obtener_FM():
    return collectionFM.find()

def obtener_FM_por_id(emisora_id):
    return collectionFM.find_one({'id': emisora_id})

def obtener_Mundo():
    return collectionMundial.find()

def obtener_Mundo_por_id(emisora_id):
    return collectionMundial.find_one({'id': emisora_id})


def obtener_Musica():
    return collectionMusica.find()

def obtener_Musica_por_id(emisora_id):
    return collectionMusica.find_one({'id': emisora_id})