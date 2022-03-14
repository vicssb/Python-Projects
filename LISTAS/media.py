''''3.	 Faça	um	programa	que	leia	4	notas,	mostre	as	notas	e	a	média	na	tela.'''

print('Programa	que	lê	4	notas,	mostre	as	notas	e	a	média	na	tela.')

notas= []
notas.append(float(input('Digite a 1a nota: ')))
notas.append(float(input('Digite a 2a nota: ')))
notas.append(float(input('Digite a 3a nota: ')))
notas.append(float(input('Digite a 4a nota: ')))

menor = 10
soma = 0
for n in notas:
    soma += n
    if n < menor:
        menor = n

media = (soma)/4



print('Sua média foi = {:.2f}'.format(media))

if media >= 6.0:
    print('APROVADO')
else:
    print('sua menor nota foi = {:.2f}'.format(menor))
    pf = float(input('digite a nota da PF: '))
    soma -= menor
    media = soma/4
    if media >= 6.0:
        print('Sua média foi = {:.2f}'.format(media))
        print('APROVADO')
    else:
        print('Sua média foi = {:.2f}'.format(media))
        print('REPROVADO')

print('fim')