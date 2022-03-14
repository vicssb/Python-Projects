'''3  Atividade
Al ́em  da  estrutura,  algumas  perguntas  devem  ser  respondidas  com  o  pro-grama.
S ̃ao elas quantos:  quantos % do terr ́ıtorio nacional  ́e ocupado por cadaestado brasileiro?
Qual foi a taxa de desmatamento total nos  ́ultimos 10 anospara cada estado e 
qual  ́e a taxa m ́edia de desmatamento para os   ́ultimos 10anos?  
Qual a taxa de desmatamento acumulado nos  ́ultimos 10 anos para cadaestado e 
qual estado que tem a maior taxa e qual tem a menor taxa?
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#leitura do arquivo de texto
valores = pd.read_csv('desmatamento.csv', ';')
print('Valores lidos:')
print(valores)
#print(valores.describe())
#print(valores.index)

#corrigindo valores
'''valoresCorrigidos = valores
for index,item in valores.iterrows():
    valoresCorrigidos['area_km2'] = item['area_km2'].replace('.','')
print('corrigidos')
print(valoresCorrigidos)
'''

# Valores dos últimos 10 anos
v_ult_10 = valores[valores['year'] >= 2010]
print('Valores dos últimos 10 anos:')
print(v_ult_10)
print('v_ult_10: ', v_ult_10.describe())
#v_ult_10['area_km2'] = v_ult_10['area_km2'].replace('.','')
#v_ult_10['area_km2'] = str(v_ult_10['area_km2']).replace('.','')
#v_ult_10['area_km2'] = pd.to_numeric(v_ult_10['area_km2'])

for index,item in v_ult_10.iterrows():
    t = item['area_km2'].replace('.','')

print('depois do numeric')
print(t)

#separando do Dataframe
anos = v_ult_10['year']
print(anos)
area = v_ult_10['area_km2']
print(area)
uf = v_ult_10['uf']
#UF sem repetições
uf2 = list(set(uf))
print(uf2)

#taxa de desmatamento total nos  ́ultimos 10 anospara cada estado
soma = 0
somas = {}
tt=[]

for est in uf2:
    print(est)
    s = v_ult_10[v_ult_10['uf'] == est]
   # print(s['area_km2'].sum())
    #soma += s['area_km2']
   # print(s['area_km2'].astype(float))
  #  s['area_km2'] = s['area_km2'].replace('.','')
    s2 = str(s['area_km2']).replace(',00', '')
    s2=s2.replace('.','')
    tt.append(s2)
    #s2 = int(s2)
    #print('S2: ',s2)
   # t = int(s2[0])
    #print('t: ',t)
    print('area_km2')
    print(s2)
    print('depois do float')
    #print(s2['area_km2'].astype(float))
    #t= int(s2['area_km2'])
    #s2['area_km2'] = pd.to_numeric(s2['area_km2'], erros = 'coerce')
    #t = int(s2[1])
    #print(s2[1].astype(float))

    print('com replace')
    print(s2[0])

    #soma += int(s2[1])

    print(soma)
    #print(s['area_km2'].replace(",","."))
    #soma = s['area_km2'].sum()
    '''    for i in s['area_km2']:
        i
        print(i)
        #soma += float(i)
        print(i.sum())
    print('soma:')
    print(soma)


    if s['uf'] == est:
        soma += v_ult_10['area_km2']
    print(soma)

    for i in v_ult_10.itertuples():
        print('for tuple')
        print(i)
        print(est)
        if i[2] == est :
            print('if uf')
            print(i[1])
'''

#print(v_ult_10)
#for i in v_ult_10.itertuples():
 #   print(i)

print('tt  ', tt)
for i in tt:
    print(i)
print(uf2)

print('Fim.')