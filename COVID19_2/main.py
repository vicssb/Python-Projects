import numpy as np
import pandas as pd

#constante
POPULACAO = 235416

#calcula a porcentagem em relação a população
def percentual(valor):
    perc = (valor * 100) / POPULACAO
    return perc

#leitura do arquivo de texto
valores = pd.read_csv("COVID19_2.csv", ';')
print('Valores lidos:')
print(valores)
print(valores.describe())
print(valores.index)

print('1 – Qual o total de profissionais da Saudade que tomaram a primeira dose de alguma vacina contra a convid-19?')
print(valores['SAUDE 1'].sum())

print('2 – Qual o total de profissionais da Saudade vacinados, ou seja, que tomaram a primeira e a segunda dose de alguma vacina contra a convid-19?')
print(valores['SAUDE 1'].sum() + valores['SAUDE 2'].sum())

print('3 – Qual a porcentagem, em relação ao total de munícipes de Jacareí, que representa os profissionais da Saudade que tomaram a primeira dose de alguma vacina contra a convid-19?')
print(percentual(valores['SAUDE 1'].sum()), ' %')

print('4 – Qual a porcentagem, em relação ao total de munícipes de Jacareí, que representa os profissionais da Saudade vacinados contra a convid-19, ou seja, que tomaram a primeira e a segunda dose de alguma vacina contra a covid-19?')
print(percentual(valores['SAUDE 1'].sum() + valores['SAUDE 2'].sum()), ' %')

print('5 – Qual o total de profissionais da Educação que tomaram a primeira dose de alguma vacina contra a convid-19?')
print(valores['EDUC 1'].sum())

print('6 – Qual o total de profissionais da Educação vacinados, ou seja, que tomaram a primeira e a segunda dose de alguma vacina contra a convid-19?')
print(valores['EDUC 1'].sum() + valores['EDUC 2'].sum())

print('7 – Qual a porcentagem, em relação ao total de munícipes de Jacareí, que representa os profissionais da Educação que tomaram a primeira dose de alguma vacina contra a convid-19?')
print(percentual(valores['EDUC 1'].sum()))

print('8 – Qual a porcentagem, em relação ao total de munícipes de Jacareí, que representa os profissionais da Educação vacinados contra a convid-19, ou seja, que tomaram a primeira e a segunda dose de alguma vacina contra a covid-19?')
print(percentual(valores['EDUC 1'].sum() + valores['EDUC 2'].sum()), ' %')

print('9 – Qual o total de idosos que tomaram a primeira dose de alguma vacina contra a convid-19?')
print(valores['IDOSO 1'].sum())

print('10 – Qual o total de idosos, ou seja, que tomaram a primeira e a segunda dose de alguma vacina contra a convid-19?')
print(valores['IDOSO 1'].sum() + valores['IDOSO 2'].sum())

print('11 – Qual a porcentagem, em relação ao total de munícipes de Jacareí, que representa os Idosos que tomaram a primeira dose de alguma vacina contra a convid-19?')
print(percentual(valores['IDOSO 1'].sum()))

print('12 – Qual a porcentagem, em relação ao total de munícipes de Jacareí, que representa os Idosos vacinados contra a convid-19, ou seja, que tomaram a primeira e a segunda dose de alguma vacina contra a covid-19?')
print(percentual(valores['IDOSO 1'].sum() + valores['IDOSO 2'].sum()), ' %')

print('13 – Qual o total de pessoas com comorbidades que tomaram a primeira dose de alguma vacina contra a convid-19?')
total_recebido = valores['CORMOB 1'].sum()
print('Total recebido: ', total_recebido)

print('14 – Qual o total de pessoas com comorbidades vacinados, ou seja, que tomaram a primeira e a segunda dose de alguma vacina contra a convid-19?')
total_recebido = valores['CORMOB 1'].sum() + valores['CORMOB 2'].sum()
print('Total recebido: ', total_recebido)

print('15 – Qual a porcentagem, em relação ao total de munícipes de Jacareí, que representa as pessoas com comorbidades que tomaram a primeira dose de alguma vacina contra a convid-19?')
porcentagem = percentual(valores['CORMOB 1'].sum())
print("A porcentagem, em relação ao total de munícipes de Jacareí: ", porcentagem, ' %')

print('16 – Qual a porcentagem, em relação ao total de munícipes de Jacareí, que representa as pessoas com comorbidades vacinados contra a convid-19, ou seja, que tomaram a primeira e a segunda dose de alguma vacina contra a covid-19?')
porcentagem = percentual(valores['CORMOB 1'].sum() + valores['CORMOB 2'].sum())
print("A porcentagem, em relação ao total de munícipes de Jacareí: ", porcentagem, ' %')

print('17 – Qual o total de vacinas aplicadas e quanto isto representa em porcentagem ao total de vacinas recebidas pelo munícipio de Jacareí?')
total_aplicado = valores['SAUDE 1'].sum() + valores['SAUDE 2'].sum() + valores['EDUC 1'].sum() + valores['EDUC 2'].sum() + valores['IDOSO 1'].sum() + valores['IDOSO 2'].sum()
print('total_aplicado: ',  total_aplicado)
total_recebido = valores['CORO 1'].sum() + valores['CORO 2'].sum() + valores['ASTRA 1'].sum() + valores['ASTRA 2'].sum()
print('Total recebido: ', total_recebido)
print('Percentual: ', total_aplicado*100/total_recebido, ' %')

print('18 – Dado que o município de Jacareí recebeu vacinas de apenas dois laboratórios até o momento, qual o total de vacinas recebidas de cada laboratório e qual o percentual de cada um em relação ao total de vacinas recebidas?')
total_recebido = valores['CORO 1'].sum() + valores['CORO 2'].sum() + valores['ASTRA 1'].sum() + valores['ASTRA 2'].sum()
print('Total recebido: ', total_recebido)
total_recebido_CORO = valores['CORO 1'].sum() + valores['CORO 2'].sum()
print('Total recebido de Coronavac: ', total_recebido_CORO)
total_recebido_ASTRA = valores['ASTRA 1'].sum() + valores['ASTRA 2'].sum()
print('Total recebido de Astrazenica: ', total_recebido_ASTRA)


print('Percentual de Coronavac: ', total_recebido_CORO*100/total_recebido, ' %')
print('Percentual de Astrazenica: ', total_recebido_ASTRA*100/total_recebido, ' %')
