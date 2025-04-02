import pandas as pd
diccionario = {"nombre":["Bryan", "Carol", "Manuel", "Scarlett", "Nicolas", "Ulises", "Geraldy"],
               "edad":[18,20,22,24,17,20,20],
               "altura":[1.8, 1.5, 1.6, 1.7, 1.8, 1.6, 1.5],
               "peso":[50, 60, 75, 80, 70, 60, 65]}

datos = pd.DataFrame(diccionario)
print(datos)