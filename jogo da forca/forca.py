print('*********************************')
print('***Bem vindo ao jogo da Forca!***')
print('****BY VICTOR********************')
print('*********************************')

palavra_secreta = 'banana'
letras_acertadas = ['_', '_', '_', '_', '_', '_']
acertou_palavra = False
enforcou = False
acertou = False
fim = False
erros = 0
MAX_ERROS = 3


while(not acertou_palavra) and (not enforcou) and (not fim):
    print("\nQual letra? ")
    print(letras_acertadas)
    letra = input("Digite uma letra ou 0 para finalizar: ")
    if letra == '0':
        fim = True
    posicao = 0
    for l in palavra_secreta:
        if (l == letra):
            letras_acertadas[posicao] = l
            print("VC acertou a letra {} na posição {} ".format(letra,posicao+1))
            acertou = True
        else:
            acertou = False
        posicao = posicao + 1
    if acertou:
        print("acertos: {}".format(letras_acertadas))
        if (letras_acertadas == palavra_secreta):
            print("VC GANHOU!!!!!!")
            fim = True
    else:
        erros = erros + 1
        print("VC errou a letra {}! Total de erros: {}".format(letra,erros))
        if (MAX_ERROS == erros):
            print("VC SE ENFORCOU!!!!!!")
            fim = True







print('\nFim do jogo')