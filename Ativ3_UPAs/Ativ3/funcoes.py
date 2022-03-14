""" Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
from math import radians, cos, sin, asin, sqrt
def haversine(lon1, lat1, lon2, lat2):

    print('haversine')
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    print('havesine'+ str(c*r))
    return c * r

'''Le o arquivo de texto com as UPAs'''
def leUPAS():
    entrada = {}
    arq = open("UPAS.txt", "r")
    linhas = arq.readlines()

    for l in linhas:
        #separa a linha em ':'
        linha = l.split(':')
        print("Linha lida:")
        print(linha)
        #preenche o dicionário entrada tirando o '\n'
        entrada[linha[0]] = linha[1].replace('\n','')

    arq.close()

    return entrada


'''Cálculo das distancias das UPAs'''
def calculoKm(lat,lon,upas):
    saidas = {}

    print('Minha posição: '+str(lat)+' - '+str(lon))
    print(upas)
    lat0 = float(lat)
    lon0 = float(lon)


    for i in upas:
        print(i)
        print(upas[i])
        posicaoUPA = upas[i]
        posicaoUPA = str(posicaoUPA).split(',')
        print('posicaoUPA')
        print(posicaoUPA)
        print(posicaoUPA[0])
        print(posicaoUPA[1])

        lat1 = float(posicaoUPA[0])
        lon1 = float(posicaoUPA[1])

        #calcular distância
        dist = haversine(lon0,lat0,lon1,lat1)
        print(dist)
        saidas[i] = dist


    return saidas




'''grava o arquivo de texto com as distancias as UPAs'''
def gravarDistancia(s):
    print('gravarDistancia')

    arq = open("Distancias_UPAS.txt", "w")
    for i in s:
        arq.write("\nDistancia de {} = ".format(i) + "{0:4.2f}".format(s[i]) + " Km")
    return ''