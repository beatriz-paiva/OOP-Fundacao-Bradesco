class Conta:

    def __init__(self, titular, numero):
        self.titular = titular
        self.numero = numero
        self.saldo = 0
        
        @property
        def saldo(self):
            return self._saldo
        
        @saldo.setter
        def saldo(self, saldo):
            if(saldo < 0):
                print("O saldo não pode ser negativo!")
            else:
                self._saldo = saldo

    
    def saque(self, valor):
        if(self.saldo>=valor):
            self.saldo -= valor
            print("Saque realizado com sucesso")
        else:
            print("Saldo insuficiente para realizar o saque")
    
    def deposita(self, valor):
        self.saldo += valor
    
    def extrato(self):
        print("\nCliente: ", self.titular, "\nSaldo Atual: ", self.saldo)