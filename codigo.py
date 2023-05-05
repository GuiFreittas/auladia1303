class ContaBancaria:
    def __init__(self, numero_conta, nome_titular, saldo=0):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente!")
        else:
            self.saldo -= valor

    def imprimir_saldo(self):
        print(f"Saldo atual da conta {self.numero_conta}: R$ {self.saldo:.2f}")

   
minha_conta = ContaBancaria("000-1", "Guilherme tem: ")


minha_conta.imprimir_saldo() 


minha_conta.depositar(113.0)
minha_conta.imprimir_saldo() 


minha_conta.sacar(700.0)
minha_conta.imprimir_saldo()  


minha_conta.sacar(2000.0)  
minha_conta.imprimir_saldo() 

