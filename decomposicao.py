import pandas as pd
import numpy as np
import matplotlib.pylab as plt 
from statsmodels.tsa.seasonal import seasonal_decompose
from pandas.plotting import register_matplotlib_converters
# Registrar conversores (caso não tenha sido feito automaticamente)
# Pode ajudar a evitar problemas com compatibilidade de versões ou configurações
register_matplotlib_converters()

dados = pd.read_csv('AirPassengers.csv')
#Conversão dos atributos que estão no formato string para formato data; Ano Mes
dados = pd.read_csv('AirPassengers.csv', parse_dates=['Month'],index_col='Month', date_format='%Y-%m')
ts = dados['#Passengers']
print(ts)
plt.plot(ts)
plt.show()

#Decomposição para visualização da tendencia e sazonalidade
decomposicao = seasonal_decompose(ts)

#Tendencia
tendencia = decomposicao.trend
plt.plot(tendencia)
plt.title('Tendencia')
plt.show()


#Sazonalidade
sazonal = decomposicao.seasonal
plt.plot(sazonal)
plt.title('Sazonalidade')
plt.show()

#Aleatoriedade
#Ruidos do grafico, onde não estava a sazionalidade nem a tendencia
# (dados que nao conseguem ser explicados matematicamente)
aleatoriedade = decomposicao.resid
plt.plot(aleatoriedade)
plt.title('Aleatoriedade')
plt.show()

#Cria uma figura em branco
plt.figure()
#plota os graficos na posição especifica subplot(*, *, *)
plt.subplot(4,1,1)
plt.plot(tendencia)
plt.title('Tendencia')
#plota os graficos na posição especifica subplot(*, *, *)
plt.subplot(4,1,2)
plt.plot(sazonal)
plt.title('Sazonalidade')
#plota os graficos na posição especifica subplot(*, *, *)
plt.subplot(4,1,3)
plt.plot(aleatoriedade)
plt.title('Aleatoriedade')
#plota os graficos na posição especifica subplot(*, *, *)
plt.subplot(4,1,4)
plt.plot(ts)
plt.title('Dados')
#Cria os graficos especificados
plt.show()