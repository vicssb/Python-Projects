import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#leitura do arquivo de texto
valores = pd.read_csv('desmatamento.csv', ';')
print('Valores lidos:')
print(valores)

#UF sem repetições
uf = valores['uf']
uf2 = list(set(uf))
print(uf2)

#corrigindo valores
valoresCorrigidos = []
temp = []
for index,item in valores.iterrows():
    t = item['area_km2'].replace(',00', '')
    tt = str(t.replace('.',''))
    valoresCorrigidos.append([item['year'], tt, item['uf']])

print('corrigidos')
print(valoresCorrigidos)

#Total do desmatamento geral
total =0
for i in valoresCorrigidos:
    total += int(i[1])
print('Total do desmatamento geral: ', total, " Km2")

#Total do desmatamento por estado
soma = 0
somaUlt10 = 0
soma2020 = 0
listaTotalDesmatamento = []
litaDesmatamentoUltimos10 = []
litaDesmatamento2020 = []
listaAnos = list(range(1988,2020,1))
listaDesmatamentoEstadoPorAno = []
#print(listaAnos)

for estado in uf2:
    for i in valoresCorrigidos:
        if estado == i[2]:
            soma += int(i[1])
            if i[0] >= 2010:
                somaUlt10 += int(i[1])
            if i[0] == 2020:
                soma2020 += int(i[1])
        #percentual
        perc = soma*100/total
        percUlt10 = somaUlt10 * 100 / total
        perc2020 = soma2020 * 100 / total

    listaTotalDesmatamento.append([estado,soma, perc])
    litaDesmatamentoUltimos10.append([estado,somaUlt10, percUlt10])
    litaDesmatamento2020.append([estado, soma2020, perc2020])
    soma = 0

print('Total do desmatamento por estado (UF, Área, %)')
#print(listaTotalDesmatamento)
for i in listaTotalDesmatamento:
    print(i[0], ", ", i[1], "Km2, {:.2f} %".format(i[2]))

eixo_x = np.array(listaTotalDesmatamento[0])
eixo_y = np.array(listaTotalDesmatamento[2])

#                    marcador / linha / cor
plt.plot(eixo_x,eixo_y,'s--g')
plt.title('Aula matplot')
plt.xlabel('Título X')
plt.ylabel('Título Y')
plt.show()

print('Desmatamento por estado últimos 10 anos (UF, Área, %)')
#print(litaDesmatamentoUltimos10)
for i in litaDesmatamentoUltimos10:
    print(i[0], ", ", i[1], "Km2, {:.2f} %".format(i[2]))

print('Desmatamento por estado último ano (UF, Área, %)')
#print(litaDesmatamento2020)
for i in litaDesmatamento2020:
    print(i[0], ", ", i[1], "Km2, {:.2f} %".format(i[2]))

#==================  numpy  ========================

print('NP')
l = np.matrix(listaTotalDesmatamento)
#l.sum(axis=0)
#s = l[:,0,:].sum()
print(l)
s = l[:,[2]]
#max = np.argmax(s)
print(s)


#==== Média ====
s = l[:,[1]]
#media = np.mean(s,dtype=np.float32)
#media = np.mean(l,axis=1)
cont = 0
soma = 0
for i in s:
    soma += float(i)
    cont += 1

media = soma / cont

print("A média de desmatamento total por estados: {:.2f} Km2".format(media))

#======================== GRAFICOS ==============================

