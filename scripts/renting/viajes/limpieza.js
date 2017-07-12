use renting
db.Archivos_Cargados.viajes.count()
db.Archivos_Cargados.viajes.remove({'Fecha inicio viaje':"NAN"})
db.Archivos_Cargados.viajes.remove({'Fecha Cumplido viaje':"NAN"})

db.Archivos_Cargados.viajes.count()
show collections
