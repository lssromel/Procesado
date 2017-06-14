from bokeh.models.widgets import Panel, Tabs
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.charts import Bar, output_file, show
from bokeh.embed import file_html
from bokeh.resources import CDN
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

db_time = user["time"]
tabla_time = db_time["viajes"]
cursor=time.find().limit(1).sort([('time', pymongo.DESCENDING)])
time=list(cursor)[0]["time"]

cursor = tabla.find()
df = pd.DataFrame(list(cursor))

output_file("prueba.html")

p = Bar(df.iloc[0:50], label='PLACA', values="Rendimiento menta combustible Meta (Km/Galon)"+str(list(cursor)[0]["time"]),agg="mean",color="PESO_BRUTO_VEH KG", plot_width=1500, plot_height=1000,
        title="Desviaciones en los precios de insumos_actividad_unidad",legend=None)
p.legend.location = "top_left"
p.legend.click_policy="hide"
tab1 = Panel(child=p, title="50")

p2 = Bar(df.iloc[0:20], label='PLACA', values="Rendimiento menta combustible Meta (Km/Galon)"+str(list(cursor)[0]["time"]),agg="mean",color="PESO_BRUTO_VEH KG", plot_width=1500, plot_height=1000,
        title="Desviaciones en los precios de insumos_actividad_unidad",legend=None)
p2.legend.location = "top_left"
p2.legend.click_policy="hide"
tab2 = Panel(child=p2, title="20")

tabs = Tabs(tabs=[ tab1, tab2 ])

html = file_html(tabs, CDN, "Prueba")

client.close()
