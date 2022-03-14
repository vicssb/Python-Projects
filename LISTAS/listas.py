'''Dada	a	lista	=	[12,	-2,	4,	8,	29,	45,	78,	36,	-17,	2,	12,	8,	3,	3,	-52]	faça	um	programa	que:
a)	imprima	o	maior	elemento
b)	imprima	o	menor	elemento
c)	imprima	os	números	pares
d)	imprima	o	número	de	ocorrências	do	primeiro	elemento	da	lista
e)	imprima	a	média	dos	elementos
f)	imprima	a	soma	dos	elementos	de	valor	negativo'''

print("A LISTA É: [12,	-2,	4,	8,	29,	45,	78,	36,	-17,	2,	12,	8,	3,	3,	-52]")
lista = [12,	-2,	4,	8,	29,	45,	78,	36,	-17,	2,	12,	8,	3,	3,	-52]
maior = max( lista)
print("o	maior	elemento É: {}".format(maior))
print("o	menor	elemento É: {}".format(min(lista)))
pares=[]
for num in lista:
    if num % 2 == 0:
        pares.append(num)
print("Elemento pares: {}".format(pares))

quant = len(lista)
soma = 0
for ele in lista:
    soma += ele
media = soma/quant
print("A média	dos	elementos: {:.2f}".format(media))

soma = 0
for elem in lista:
    if elem < 0:
        soma += elem
print("A soma	dos	elementos	de	valor	negativo: {}".format(soma))
