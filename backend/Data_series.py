# Importar librerias
import pandas as pd
import numpy as np
import yfinance as yf 
import quandl
from datetime import datetime, timedelta
from companies_dict import companies_dict

# Configurar la clave de Quandl para descargar indices financieros
QUANDL_API_KEY ='85zxshzz6QfYYzu-sf-z'
quandl.ApiConfig.api_key = QUANDL_API_KEY

# Descargar los datos y mantener solo precios de cierre ajustados
user = input('Elija una empresa  ')
companyName = user.title()

company = companies_dict[companyName] # company es el ticker 

today = datetime.now()
year_ago = today - timedelta(days=365)


df = yf.download(company,
            start= year_ago,
            end= today,
            progress=False)
df = df.loc[:, ['Adj Close']]
df.rename(columns={'Adj Close':'adj_close'}, inplace=True)

# Calcule los rendimientos simples y logaritmicos
df['simple_rtn'] = df.adj_close.pct_change()
df['log_rtn'] = np.log(df.adj_close/df.adj_close.shift(1))

# Se importan las librerias de graficos
import matplotlib.pyplot as plt
import warnings

fig, ax = plt.subplots(3, 1, figsize=(12, 10), sharex=True)

# Agregar precios y rendimientos a la gráfica
df.adj_close.plot(ax=ax[0])
ax[0].set(title = companyName +' Time series',
            ylabel = 'Stock price ($)')

df.simple_rtn.plot(ax=ax[1])
ax[1].set(ylabel = 'Simple returns (%)')

df.log_rtn.plot(ax=ax[2])
ax[2].set(ylabel = 'Log returns (%)')

ax[2].tick_params(axis='x',
                which='major',
                labelsize=12)

plt.tight_layout()
#plt.savefig(companyName+'_ds.png')
plt.show()