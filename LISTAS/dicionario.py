'''Faça	um	programa	utilizando	um		dict		que	leia	dados	de	entrada	do	usuário.	O	usuário	deve	entrar
com	os	dados	 de	 uma	 pessoa	 como	 nome,	idade	 e	 cidade	 onde	mora	 (fique	livre	 para	 acrescentar
outros).	Após	isso,	você	deve	imprimir	os	dados	como	o	exemplo	abaixo:
					nome:	João
					idade:	20
					cidade:	São	Paulo'''

print('CRIA UM DICIONÁRIO')
resp = 's'
while resp == 's':
    nomeI = input('Digite seu nome: ')
    idadeI = input('Digite sua idade: ')
    cidadeI = input('Digite sua cidade: ')

    dicionario = dict(nome = nomeI,idade = idadeI, cidade = cidadeI)

    print('O nome é {}'.format(dicionario['nome']))
    print('A idade é {}'.format(dicionario['idade']))
    print('A cidade é {}'.format(dicionario['cidade']))

    lista = []
    lista.append(dicionario)
    resp = input('Deseja continuar? s ou n ')

for elem in lista:
    print('O nome é {}'.format(elem['nome']))

print('fim')