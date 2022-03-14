'''2  AtividadeNo c ́odigo, existe uma Series com notas de alguns alunos.
 Utilizando os recursosda biblioteca pandas imprima a menor nota, a maior nota e a m ́edia da turma.
 import pandas as pdnotas = pd.Series([2,7,5,10,6], index=["Joao", "Maria", "Luiz", "Julia", "Daniel"])'''

import pandas as pd
notas = pd.Series([2,7,5,10,6], index=["Joao", "Maria", "Luiz", "Julia", "Daniel"])

print('a menor nota:')
print(notas.min())
print('a maior nota:')
print(notas.max())
print('a média das nota:')
print(notas.mean())

print('Fim.')