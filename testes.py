# se
# pm shell

from django.conf import settings

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import binom, norm, mannwhitneyu, ttest_ind
from statsmodels.stats.power import TTestIndPower

import io
import base64
import matplotlib.pyplot as plt
import seaborn as sns

from pymongo.mongo_client import MongoClient
uri = settings.DATABASES['mongo']['URI']
client = MongoClient(uri)
dba = client['db_teste']

col = dba['population']
df_ori = pd.DataFrame(col.find({}))

df_work = df_ori[['city', 'date', 'count']]
df_work['type'] = df_work.apply(lambda x: 'processos' if 'total' in x['city'] else 'cancelados', axis=1)
df_work['city'] = df_work.apply(lambda x: x['city'].replace('_total', '').replace('_cancel', '').upper(), axis=1)





df_mes = df_work.groupby(by=['type', 'city', df_work['date'].dt.to_period('M')])['count'].sum().reset_index()
df_mes['ano'] = df_mes['date'].dt.year
df_mes['mes'] = df_mes['date'].dt.month






print(df_work.shape)
df_work.head()
print(df_mes.shape)
df_mes.head()

plt.figure(figsize=(9, 6))
sns.barplot(data=df_mes, x='city', y='count', hue="type", palette="dark", alpha=.6, ci = 0)
plt.title('Média de Processos e Cancelamentos por Mês')
plt.xlabel('Cidade')
plt.ylabel('')
plt.legend(title='')
plt.show()