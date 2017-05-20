
import pandas as pd
from pymongo import MongoClient
import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read("/workspace/Procesado/mongo.ini")
ip = Config.get("Mongo","ip")
port = Config.get("Mongo","port")

client = MongoClient(host=(str(ip)+":"+str(port)))

user=client["renting"]
archivos_cargados=user["Archivos_Cargados"]
tabla=archivos_cargados["viajes"]

cursor = tabla.find()
df = pd.DataFrame(list(cursor))

for i in range(len(df)):
    tabla.update_one({"_id":df.iloc[i]["_id"]},{"$set":{"prueba2":df.iloc[i]["kilometros"]/i+1}})

client.close()
