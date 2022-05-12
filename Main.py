from Connexion import db
from bson.objectid import ObjectId
from pprint import pprint

# Requête 1 V2
cursor = db.etudiants.find({"nom": "Boris Karloff"})
cursor = cursor[0]

sum = 0
nb = 0

for ue in cursor["UE"]:
    nb += 1
    sum += ue["note"]
pprint(f"moyenne : {(sum/nb)}")