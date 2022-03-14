#ler a partir de uma arquivo de texto
# todas as upas e suas respectiva coordenadas
# a formula haversine km --> 1000m
# def calculoKm(lat,lon)
# novo dicionario:
# distancias = {nome_upa : distancia em km}


#importa as operações
import funcoes as f

#minha posicao
minhaPosicao = [-23.268878905538553, -45.92259903136803]

print('Cálculo distancias UPAs')
#lê o arquivo TXT com as UPAs
entrada = f.leUPAS()

print('Dicionário das UPAs:')
print(entrada)

nome = []
posicao = []
for i in entrada:
    nome.append(i)
    posicao.append(entrada[i])

print('Lista dos nomes:')
print(nome)
print('Lista das posições:')
print(posicao)
print('\n')


#calcular as distâncias
distancias = {}

d = f.calculoKm(minhaPosicao[0],minhaPosicao[1],entrada)

print('Main: DistÂncias UPas')
print(d)

#gravarDistancia em TXT
f.gravarDistancia(d)




print('Fim PRG.')