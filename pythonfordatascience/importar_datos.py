import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


estadisticas = pd.read_csv("P4-Demographic-Data.csv")

estadisticas.columns = ["CountryName","CountryCode","BirthRate","InternetUsers","IncomeGroup"]


sns.lmplot(x = 'InternetUsers', y = 'BirthRate', data = estadisticas, fit_reg = False, hue = 'IncomeGroup')
plt.show()

#Analizando el set de Datos
#1.-Ver el full set
# print(estadisticas)

#2.-Numero de filas
#print(len(estadisticas))

#3.-Ver columnas
#print(estadisticas.columns)

#4.-Ver numero de columnas
#print(len(estadisticas.columns))

#5.-Fila de Arriba(Cabecera)
#print(estadisticas.head(5))

#6.- Fila de Abajo (Footer)
#print(estadisticas.tail(5))

#7.-Informacion de las columnas
#print(estadisticas.info())

#8.- Estadisticas Columnas
#print(estadisticas.describe())