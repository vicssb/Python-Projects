'''1  AtividadeNo c ́odigo, existem sequˆencias de n ́umeros.
Coloque cada uma delas dentro de uma estrutura do tipo Series e mostre informa ̧c ̃oes como,
 m ́edia, maior valor emenor valor. Al ́em disto, mostre em quais indices est ̃ao cada elemento
  e tamb ́emselecione e imprima o terceiro elemento de cada sequˆencia.
  s1 = [1,2,3,4,5,6]s2 = [-0.5,-0.3,1,-1.5]'''

import pandas as pd

s1 = pd.Series([1,2,3,4,5,6])
s2 = pd.Series([-0.5,-0.3,1,-1.5])

print('Série 1:')
print(s1)
print('Série 2:')
print(s2)

print('Média da Série 1:')
print(s1.mean())
print('Média da Série 2:')
print(s2.mean())
print('Max da Série 1:')
print(s1.max())
print('Max da Série 2:')
print(s2.max())
print('Min da Série 1:')
print(s1.min())
print('Min da Série 2:')
print(s2.min())
print('3o elemento da Série 1:')
print(s1[2])
print('3o elemento da Série 2:')
print(s2[2])


print('Fim.')