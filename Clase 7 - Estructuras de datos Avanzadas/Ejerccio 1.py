"""Creando un dataframe

Instale la biblioteca pandas e impórtela en su proyecto Python.
Cree un dataframe con un diccionario, tal como se vio en los ejemplos, con las siguientes columnas, y con 5 datos:
Nombre
Rut
Edad
Altura
Peso
Describa y discuta los datos almacenados en el dataframe (almacene los ruts como strings)."""

""" en el terminal: 

-  activar el ambiente virtual: activar un entorno virtual en PowerShell en Windows, debes usar este comando:
.venv\Scripts\Activate.ps1

- Intalar Pandas: 
pip install pandas

- Para instalar ipython en tu entorno virtual
pip install ipython

Una vez termine de instalarse, podrás usar ipython directamente:
- ipython

import pandas as pd
data = {
    'Nombre': ['Ana', 'Maria', 'Sofía', 'Luisa', 'Josefa'],
    'Rut': ['12446500-1', '12181181-2', '11004663-4', '13940675-3', '17027199-8'],
    'Edad': [22, 35, 12, 32, 45],
    'Altura': [1.6, 1.7, 1.6, 1.7, 1.6],
    'Peso': [65, 42, 64, 74, 62]
}
df = pd.DataFrame(data)
revisión de los datos con head

df.head()
Nombre	Rut	Edad	Altura	Peso
0	Ana	12446500-1	22	1.6	65
1	Maria	12181181-2	35	1.7	42
2	Sofía	11004663-4	12	1.6	64
3	Luisa	13940675-3	32	1.7	74
4	Josefa	17027199-8	45	1.6	62
Mostrar el DataFrame

print(df)
   Nombre         Rut  Edad  Altura  Peso
0     Ana  12446500-1    22     1.6    65
1   Maria  12181181-2    35     1.7    42
2   Sofía  11004663-4    12     1.6    64
3   Luisa  13940675-3    32     1.7    74
4  Josefa  17027199-8    45     1.6    62
Descripción del DataFrame:

df.describe()
Edad	Altura	Peso
count	5.000000	5.000000	5.000000
mean	29.200000	1.640000	61.400000
std	12.637247	0.054772	11.781341
min	12.000000	1.600000	42.000000
25%	22.000000	1.600000	62.000000
50%	32.000000	1.600000	64.000000
75%	35.000000	1.700000	65.000000
max	45.000000	1.700000	74.000000
Mostrar información del DataFrame

df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 5 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   Nombre  5 non-null      object 
 1   Rut     5 non-null      object 
 2   Edad    5 non-null      int64  
 3   Altura  5 non-null      float64
 4   Peso    5 non-null      int64  
dtypes: float64(1), int64(2), object(2)
memory usage: 328.0+ bytes

"""