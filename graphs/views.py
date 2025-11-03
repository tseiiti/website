from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings

import io
import base64
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from pymongo.mongo_client import MongoClient
uri = settings.DATABASES['mongo']['URI']
client = MongoClient(uri)
dba = client['db_teste']

params = { "sidenav": settings.SIDENAV }



def df_aux_01():
  pip = [
    { '$project': {
      'city': 1,
      'type': 1,
      'count': 1,
      'date': { '$dateToString': { 'format': '%Y-%m', 'date': '$date' } },
      'ano': { '$dateToString': { 'format': '%Y', 'date': '$date' } },
      'mes': { '$dateToString': { 'format': '%m', 'date': '$date' } }, }},
    { '$group': {
      '_id': { 'city': '$city', 'type': '$type', 'date': '$date', 'ano': '$ano', 'mes': '$mes' },
      'count': { '$sum': '$count' } }},
    { '$project': {
      '_id': 0,
      'city': '$_id.city',
      'type': '$_id.type',
      'date': '$_id.date',
      'ano': '$_id.ano',
      'mes': '$_id.mes',
      'count': 1, }},
    { '$sort' : {
      'city' : 1, 'type': -1 }},
  ]
  df = pd.DataFrame(dba['population'].aggregate(pip))
  return df

def df_aux_03():
  df = df_aux_01()
  df_ce = df.query("city == 'CE'").pivot_table(index='date', columns='type', values='count', fill_value=0).astype(int)
  df_ce['ind'] = df_ce.apply(lambda x: round(x['Cancelados'] / x['Total'] * 100.0, 2), axis=1)
  df_co = df.query("city == 'CO'").pivot_table(index='date', columns='type', values='count', fill_value=0).astype(int)
  df_co['ind'] = df_co.apply(lambda x: round(x['Cancelados'] / x['Total'] * 100.0, 2), axis=1)
  df_ex = df.query("city == 'EX'").pivot_table(index='date', columns='type', values='count', fill_value=0).astype(int)
  df_ex['ind'] = df_ex.apply(lambda x: round(x['Cancelados'] / x['Total'] * 100.0, 2), axis=1)
  df_ol = df.query("city == 'OL'").pivot_table(index='date', columns='type', values='count', fill_value=0).astype(int)
  df_ol['ind'] = df_ol.apply(lambda x: round(x['Cancelados'] / x['Total'] * 100.0, 2), axis=1)
  df_sa = df.query("city == 'SA'").pivot_table(index='date', columns='type', values='count', fill_value=0).astype(int)
  df_sa['ind'] = df_sa.apply(lambda x: round(x['Cancelados'] / x['Total'] * 100.0, 2), axis=1)
  df_su = df.query("city == 'SU'").pivot_table(index='date', columns='type', values='count', fill_value=0).astype(int)
  df_su['ind'] = df_su.apply(lambda x: round(x['Cancelados'] / x['Total'] * 100.0, 2), axis=1)

  df = pd.DataFrame({
    'CE': df_ce['ind'],
    'CO': df_co['ind'],
    'EX': df_ex['ind'],
    'OL': df_ol['ind'],
    'SA': df_sa['ind'],
    'SU': df_su['ind']
  })
  df = df.melt(var_name='cidade', value_name='Total')
  return df

def graph_aux(plt):
  buffer = io.BytesIO()
  plt.savefig(buffer, format='png')
  buffer.seek(0)
  plt.close()

  image = buffer.getvalue()
  graph = base64.b64encode(image)
  return graph.decode('utf-8')

@login_required
def graph_01(request):
  df = df_aux_01()

  plt.figure(figsize=(9, 6))
  sns.barplot(data=df, x='city', y='count', hue="type", palette="dark", alpha=.6, errorbar=('ci', 0))
  plt.title('Média de Processos e Cancelamentos por Mês')
  plt.xlabel('Cidades')
  plt.ylabel('')
  plt.legend(title='')

  pip = [
    { '$group': {
      '_id': { 'type': '$type' },
      'count': { '$sum': '$count' } }},
    { '$project': {
      '_id': 0,
      'type': '$_id.type',
      'count': 1, }},
    { '$sort' : {
      'type': -1 }},
  ]

  params["user"] = request.user
  params["items"] = dba['population'].aggregate(pip)
  params["graph"] = graph_aux(plt)
  return render(request, "graphs/graph_01.html", params)

@login_required
def graph_02(request):
  city = request.GET.get("city") or "SA"
  df = df_aux_01().query(f"city == '{city}'")

  plt.figure(figsize=(9, 6))
  sns.set_theme(style="ticks", palette="pastel")
  g = sns.boxplot(x="city", y="count", hue="type", data=df)
  g.tick_params(bottom=False, labelbottom=False)
  sns.despine(offset=10, trim=True)
  plt.xlabel('')
  plt.ylabel('')
  plt.legend(title='')

  params["title_1"] = f'Boxblot de Cancelamentos e Processos por Mês em "{ city }"'
  params["user"] = request.user
  params["graph"] = graph_aux(plt)
  params["city"] = city
  return render(request, "graphs/graph_02.html", params)

@login_required
def graph_03(request):
  pip = [
    { '$group': {
      '_id': { 'city': '$city', 'type': '$type', 'date': '$date' },
      'count': { '$sum': '$count' } }},
    { '$project': {
      '_id': 0,
      'city': '$_id.city',
      'type': '$_id.type',
      'date': '$_id.date',
      'count': 1, }},
    { '$sort' : {
      'city' : 1, 'type': -1 }},
  ]
  df_work = pd.DataFrame(dba['population'].aggregate(pip))
  
  params["items"] = []
  for city in ['CE', 'CO', 'EX', 'OL', 'SA', 'SU']:
    df = df_work.query(f"city == '{city}'")
    plt.figure(figsize=(9, 6))
    df = df.pivot_table(index='date', columns='type', values='count', fill_value=0)
    df.plot(kind='scatter', x='Total', y='Cancelados', s=32, alpha=.8, xlabel='Processos', ylabel='Cancelamentos')
    plt.title(f'Dispersão da cidade "{ city }"')
    plt.gca().spines[['top', 'right',]].set_visible(False)
    params["items"].append(graph_aux(plt))
    
  params["title_1"] = f'Dispersão entre Processos e Cancelamentos por dia'
  params["user"] = request.user
  return render(request, "graphs/graph_03.html", params)

@login_required
def graph_04(request):
  df = df_aux_03()
  plt.figure(figsize=(12, 6))
  sns.kdeplot(data=df, x='Total', hue='cidade', fill=True, palette='dark')
  plt.xlabel('Índices')
  plt.ylabel('')
    
  params["title_1"] = 'Comparando a densidade dos índices de cancelamento dos processos'
  params["user"] = request.user
  params["graph"] = graph_aux(plt)
  return render(request, "graphs/graph_04.html", params)

# @login_required
def powerbi(request):
  params["title"] = "Power BI"
  params["user"] = request.user
  return render(request, "graphs/powerbi.html", params)
