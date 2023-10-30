print("Testando o projeto")
from Cliente import Cliente
from Conta import Conta

c1 = Cliente("João", "114444-2222")
conta = Conta(c1.get_nome(), 1222)
print("Estado Inicial da Conta: ")
print(conta.titular, " Número: ", conta.numero,
"\n Seu Saldo: ", conta.saldo)

conta.deposita(100)
conta.saque(50)
conta.extrato()