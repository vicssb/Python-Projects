'''Defina uma função chamada velocidade_media() em um script chamado funcoes.py que recebe
dois parâmetros: a distância percorrida (em metros) e o tempo (em segundos) gasto.'''

def velocMedia(distancia, tempo):
    vm = distancia/tempo
    return (vm)

def soma(n1,n2):
    return(n1+n2)

def subtracao(n1,n2):
    return (n1-n2)

def calculadora(x,y):
    return {'soma':soma(x,y), 'subtração':subtracao(x,y), 'multiplicação':x*y, 'divisão':x/y}

num1 = 100
num2 = 20

print ('A velociade média é = {:.2f}'.format(velocMedia(num1,num2)))
print('A soma de {} e de {} é = {}'.format(num1,num2,soma(num1,num2)))
print('A diferença de {} e de {} é = {}'.format(num1,num2,subtracao(num1,num2)))

resultados = calculadora(num1,num2)
for key in resultados:
 print('{}: {}'.format(key, resultados[key]))


def teste_args_kwargs(**kwargs):
    for key, value in kwargs.items():
        print('{0} = {1}'.format(key, value))

dicionario = {'arg1': 'joao', 'arg2': 25, 'arg3':'RJ', 'arg4':4}
teste_args_kwargs(**dicionario)