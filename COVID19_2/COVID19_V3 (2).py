#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
projeto COVID 19

1 – Qual o total de profissionais da Saudade que tomaram a primeira dose de alguma vacina contra a convid-19?

2 – Qual o total de profissionais da Saudade vacinados, ou seja, que tomaram a primeira e a segunda dose de alguma vacina contra a convid-19?

3 – Qual a porcentagem, em relação ao total de munícipes de Jacareí, que representa os profissionais da Saudade que tomaram a primeira dose de alguma vacina contra a convid-19?

4 – Qual a porcentagem, em relação ao total de munícipes de Jacareí, que representa os profissionais da Saudade vacinados contra a convid-19, ou seja, que tomaram a primeira e a segunda dose de alguma vacina contra a covid-19?

5 – Qual o total de profissionais da Educação que tomaram a primeira dose de alguma vacina contra a convid-19?

6 – Qual o total de profissionais da Educação vacinados, ou seja, que tomaram a primeira e a segunda dose de alguma vacina contra a convid-19?

7 – Qual a porcentagem, em relação ao total de munícipes de Jacareí, que representa os profissionais da Educação que tomaram a primeira dose de alguma vacina contra a convid-19?

8 – Qual a porcentagem, em relação ao total de munícipes de Jacareí, que representa os profissionais da Educação vacinados contra a convid-19, ou seja, que tomaram a primeira e a segunda dose de alguma vacina contra a covid-19?

9 – Qual o total de idosos que tomaram a primeira dose de alguma vacina contra a convid-19?

10 – Qual o total de idosos, ou seja, que tomaram a primeira e a segunda dose de alguma vacina contra a convid-19?

11 – Qual a porcentagem, em relação ao total de munícipes de Jacareí, que representa os Idosos que tomaram a primeira dose de alguma vacina contra a convid-19?

12 – Qual a porcentagem, em relação ao total de munícipes de Jacareí, que representa os Idosos vacinados contra a convid-19, ou seja, que tomaram a primeira e a segunda dose de alguma vacina contra a covid-19?

13 – Qual o total de pessoas com comorbidades que tomaram a primeira dose de alguma vacina contra a convid-19?

14 – Qual o total de pessoas com comorbidades vacinados, ou seja, que tomaram a primeira e a segunda dose de alguma vacina contra a convid-19?

15 – Qual a porcentagem, em relação ao total de munícipes de Jacareí, que representa as pessoas com comorbidades que tomaram a primeira dose de alguma vacina contra a convid-19?

16 – Qual a porcentagem, em relação ao total de munícipes de Jacareí, que representa as pessoas com comorbidades vacinados contra a convid-19, ou seja, que tomaram a primeira e a segunda dose de alguma vacina contra a covid-19?

17 – Qual o total de vacinas aplicadas e quanto isto representa em porcentagem ao total de vacinas recebidas pelo munícipio de Jacareí?

18 – Dado que o município de Jacareí recebeu vacinas de apenas dois laboratórios até o momento, qual o total de vacinas recebidas de cada laboratório e qual o percentual de cada um em relação ao total de vacinas recebidas?'''


# In[2]:


print('COVID 19')


# In[3]:


import pandas as pd


# In[4]:


#constante
POPULACAO = 235416


# In[5]:


#calcula a porcentagem em relação a população
def percentual(valor):
    perc = (valor * 100) / POPULACAO
    return perc


# In[6]:


#leitura do arquivo de texto
valores = pd.read_csv("COVID19.CSV", ';')
print('Valores lidos:')
#print(valores)
print(valores.describe())
print(valores.index)


# In[7]:


print('1 – Qual o total de profissionais da Saudade que tomaram a primeira dose de alguma vacina contra a convid-19?')
print(valores['SAUDE 1'].sum())


# In[8]:


print('2 – Qual o total de profissionais da Saudade vacinados, ou seja, que tomaram a primeira e a segunda dose de alguma vacina contra a convid-19?')
print(valores['SAUDE 1'].sum() + valores['SAUDE 2'].sum())


# In[33]:


print('3 – Qual a porcentagem, em relação ao total de munícipes de Jacareí, que representa os profissionais da Saudade que tomaram a primeira dose de alguma vacina contra a convid-19?')
print("A porcentagem é: {:.2f} %".format(percentual(valores['SAUDE 1'].sum())))


# In[32]:


print('4 – Qual a porcentagem, em relação ao total de munícipes de Jacareí, que representa os profissionais da Saudade vacinados contra a convid-19, ou seja, que tomaram a primeira e a segunda dose de alguma vacina contra a covid-19?')
print("A porcentagem é: {:.2f} %".format(percentual(valores['SAUDE 1'].sum() + valores['SAUDE 2'].sum())))


# In[11]:


print('5 – Qual o total de profissionais da Educação que tomaram a primeira dose de alguma vacina contra a convid-19?')
print(valores['EDUC 1'].sum())


# In[12]:


print('6 – Qual o total de profissionais da Educação vacinados, ou seja, que tomaram a primeira e a segunda dose de alguma vacina contra a convid-19?')
print(valores['EDUC 1'].sum() + valores['EDUC 2'].sum())


# In[31]:


print('7 – Qual a porcentagem, em relação ao total de munícipes de Jacareí, que representa os profissionais da Educação que tomaram a primeira dose de alguma vacina contra a convid-19?')
print("A porcentagem é: {:.2f} %".format(percentual(valores['EDUC 1'].sum())))


# In[30]:


print('8 – Qual a porcentagem, em relação ao total de munícipes de Jacareí, que representa os profissionais da Educação vacinados contra a convid-19, ou seja, que tomaram a primeira e a segunda dose de alguma vacina contra a covid-19?')
print("A porcentagem é: {:.2f} %".format(percentual(valores['EDUC 1'].sum() + valores['EDUC 2'].sum())))


# In[15]:


print('9 – Qual o total de idosos que tomaram a primeira dose de alguma vacina contra a convid-19?')
print(valores['IDOSO 1'].sum())


# In[16]:


print('10 – Qual o total de idosos, ou seja, que tomaram a primeira e a segunda dose de alguma vacina contra a convid-19?')
print(valores['IDOSO 1'].sum() + valores['IDOSO 2'].sum())


# In[29]:


print('11 – Qual a porcentagem, em relação ao total de munícipes de Jacareí, que representa os Idosos que tomaram a primeira dose de alguma vacina contra a convid-19?')
print("A porcentagem é: {:.2f} %".format(percentual(valores['IDOSO 1'].sum())))


# In[28]:


print('12 – Qual a porcentagem, em relação ao total de munícipes de Jacareí, que representa os Idosos vacinados contra a convid-19, ou seja, que tomaram a primeira e a segunda dose de alguma vacina contra a covid-19?')
print("A porcentagem é: {:.2f} %".format(percentual(valores['IDOSO 1'].sum() + valores['IDOSO 2'].sum())))


# In[19]:


print('13 – Qual o total de pessoas com comorbidades que tomaram a primeira dose de alguma vacina contra a convid-19?')
total_recebido = valores['CORMOB 1'].sum()
print('Total recebido: ', total_recebido)


# In[20]:


print('14 – Qual o total de pessoas com comorbidades vacinados, ou seja, que tomaram a primeira e a segunda dose de alguma vacina contra a convid-19?')
total_recebido = valores['CORMOB 1'].sum() + valores['CORMOB 2'].sum()
print('Total recebido: ', total_recebido)


# In[27]:


print('15 – Qual a porcentagem, em relação ao total de munícipes de Jacareí, que representa as pessoas com comorbidades que tomaram a primeira dose de alguma vacina contra a convid-19?')
porcentagem = percentual(valores['CORMOB 1'].sum())
print("A porcentagem, em relação ao total de munícipes de Jacareí: {:.2f} %".format(porcentagem))


# In[26]:


print('16 – Qual a porcentagem, em relação ao total de munícipes de Jacareí, que representa as pessoas com comorbidades vacinados contra a convid-19, ou seja, que tomaram a primeira e a segunda dose de alguma vacina contra a covid-19?')
porcentagem = percentual(valores['CORMOB 1'].sum() + valores['CORMOB 2'].sum())
print("A porcentagem, em relação ao total de munícipes de Jacareí: {:.2f} %".format(porcentagem))


# In[25]:


print('17 – Qual o total de vacinas aplicadas e quanto isto representa em porcentagem ao total de vacinas recebidas pelo munícipio de Jacareí?')
total_aplicado = valores['SAUDE 1'].sum() + valores['SAUDE 2'].sum() + valores['EDUC 1'].sum() + valores['EDUC 2'].sum() + valores['IDOSO 1'].sum() + valores['IDOSO 2'].sum()
print('total_aplicado: ',  total_aplicado)
total_recebido = valores['CORO 1'].sum() + valores['CORO 2'].sum() + valores['ASTRA 1'].sum() + valores['ASTRA 2'].sum()
print('Total recebido: ', total_recebido)
print('Percentual: {:.2f} %'.format( total_aplicado*100/total_recebido, ' %'))


# In[24]:


print('18 – Dado que o município de Jacareí recebeu vacinas de apenas dois laboratórios até o momento, qual o total de vacinas recebidas de cada laboratório e qual o percentual de cada um em relação ao total de vacinas recebidas?')
total_recebido = valores['CORO 1'].sum() + valores['CORO 2'].sum() + valores['ASTRA 1'].sum() + valores['ASTRA 2'].sum()
total_recebido = int(total_recebido )
print('Total recebido0: %d'% total_recebido)
print('Total recebido: {0:,}'.format(total_recebido))

print('Total recebido: {0:,}'.format(total_recebido).replace(',','.'))

total_recebido_CORO = valores['CORO 1'].sum() + valores['CORO 2'].sum()
#total_recebido_CORO = int(total_recebido_CORO)
print(type(total_recebido_CORO))
print('Total recebido de Coronavac: {:.0f}'.format(total_recebido_CORO))
total_recebido_ASTRA = valores['ASTRA 1'].sum() + valores['ASTRA 2'].sum()
print('Total recebido de Astrazenica: ', total_recebido_ASTRA)


print('Percentual de Coronavac: {:.2f} %'.format(total_recebido_CORO*100/total_recebido, ' %'))
print('Percentual de Astrazenica: {:.2f} %'.format( total_recebido_ASTRA*100/total_recebido, ' %'))

# In[ ]:




