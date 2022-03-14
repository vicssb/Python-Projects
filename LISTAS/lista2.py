'''Faça	 um	 programa	 que	 leia	 dados	 do	 usuário	 (nome,	 sobrenome,	idade)	 adicione	 em	 uma	 lista	 e
imprima	seus	elementos	na	tela.'''

print("Faça	 um	 programa	 que	 leia	 dados	 do	 usuário	 (nome,	 sobrenome,	idade)	 adicione	 em	 uma	 lista	 e imprima	seus	elementos	na	tela.")

lista=[]

lista.append(input('Didite seu nome: '))
lista.append(input('Didite seu sobrenome: '))
lista.append(input('Didite sua idade: '))

print('\nSeu nome é: {}'.format(lista[0]))
print('Seu sobrenome é: {}'.format(lista[1]))
print('Sua idade é: {}'.format(lista[2]))