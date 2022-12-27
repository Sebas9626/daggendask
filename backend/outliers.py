import pandas
import yfinance as yf 
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from companies_dict import companies_dict

user = input('Elija una empresa  ')
companyName = user.title()
company = companies_dict[companyName] # company es el ticker 

today = datetime.now()
year_ago = today - timedelta(days=180)

# Descargar los datos y mantener solo precios de cierre ajustados
df = yf.download(company,
            start=year_ago,
            end=today,
            progress=False)
df = df.loc[:, ['Adj Close']]
df.rename(columns={'Adj Close':'adj_close'}, inplace=True)

# Calcule los rendimientos simples 
df['simple_rtn'] = df.adj_close.pct_change()

# Calcule la media movil y desviación estandar
df_rolling = df[['simple_rtn']].rolling(window=21) \
                             .agg(['mean','std'])
df_rolling.columns = df_rolling.columns.droplevel()

# Unir medias moviles a los datos de cierre
df_outliers = df.join(df_rolling)

# Se define la función 3 sigma para detectar valores atípicos
def identify_outliers(row, n_sigmas=3):
    # Pagina 136
    x = row['simple_rtn']
    mu = row['mean']
    sigma = row['std']

    if (x > mu + 3 * sigma) | (x < mu - 3 * sigma):
        return 1
    else:
        return 0

# Identificar los valores atipicos y extraer sus valores
df_outliers['outlier'] = df_outliers.apply(identify_outliers,
                                            axis=1)
outliers = df_outliers.loc[df_outliers['outlier'] == 1,
                            ['simple_rtn']]

# Graficar los resultados
fig, ax = plt.subplots()
ax.plot(df_outliers.index, df_outliers.simple_rtn,
        color='blue', label='Normal')
ax.scatter(outliers.index, outliers.simple_rtn,
        color='red', label='Anomaly')
ax.set_title(companyName+"'s stock returns")
ax.legend(loc='lower right')

plt.show()
