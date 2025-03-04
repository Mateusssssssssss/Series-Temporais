import pandas as pd
import numpy as np
import matplotlib.pylab as plt 
from datetime import datetime
from pandas.plotting import register_matplotlib_converters
# Registrar conversores (caso não tenha sido feito automaticamente)
# Pode ajudar a evitar problemas com compatibilidade de versões ou configurações
register_matplotlib_converters()
#Ler os dados
dados = pd.read_csv('AirPassengers.csv')
#Ler as 5 primeiras linhas
print(dados.head())
#Tipo dos dados do dataset
print(dados.dtypes)
#Conversão dos atributos que estão no formato string para formato data; Ano Mes
dateparse = lambda dates: datetime.strptime(dates, '%Y-%m')
dados = pd.read_csv('AirPassengers.csv', parse_dates=['Month'],index_col='Month', date_parser = dateparse)
print(dados.head())
print(dados.index)

ts = dados['#Passengers']
print(ts)

#Visualização por ano e mes
print(ts['1949-02'])

#Visualização de data especifica
print(ts[datetime(1949,2,1)])

#Visualização por intervalo
print(ts['1950-01-01':'1950-07-31'])

#Visualização sem data de inicio
print(ts[:'1950-07-31'])
#visualização por ano
print(ts['1950'])
#Valores maximos
print(ts.index.max())
#Valores minimos
print(ts.index.min())

#Grafico
plt.plot(ts)
plt.show()
#grafico por ano
ts_ano = ts.resample('YE').sum()
plt.plot(ts_ano)
plt.show()
#Grafico por mes
ts_mes = ts.groupby([lambda x:x.month]).sum()
plt.plot(ts_mes)
plt.show()

#Grafico entre datas especificas
ts_dates = ts['1960-01-01':'1960-12-01']
plt.plot(ts_dates)
plt.show()