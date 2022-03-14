class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("inicializando uma conta")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            return True

    def extrato(self):
        print("numero: {} \nsaldo: {}".format(self.numero, self.saldo))