#IMPORT
from pymongo import MongoClient

# VARIABLE
IP="mongo2.iem"
PORT=27017
USERNAME="ch098407"
PASSWORD="ch098407"
AUTHSOURCE= "ch098407"

#Connexion à la base de données
c=MongoClient(IP, port=PORT, username=USERNAME, password=PASSWORD, authSource=AUTHSOURCE, authMechanism="SCRAM-SHA-1")
db=c.ch098407
