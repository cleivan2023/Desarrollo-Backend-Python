""" Incorpore el siguiente código en su IDE y estúdielo"""

FIN = False
registro_llamado = {"frecuencia": None, "motivo": None, "fecha": None}
listado_llamados = []
while not FIN:
  frecuencia = input("Ingrese frecuencia: ")
  if frecuencia == "FIN":
    FIN = True
  else:
    motivo = input("Ingrese motivo: ")
    fecha = input("Ingrese fecha: ")
    registro_llamado["frecuencia"] = frecuencia
    registro_llamado["motivo"] = motivo
    registro_llamado["fecha"] = fecha
    listado_llamados.append(registro_llamado)
print(listado_llamados)