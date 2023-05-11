class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo
        self.depositos = []
        self.saques = []
        self.num_saques = 0
    
    def depositar(self, valor):
        if valor > 0:
            self.depositos.append(valor)
            self.saldo += valor
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('Valor inválido para depósito.')
    
    def sacar(self, valor):
        if valor <= 0:
            print('Valor inválido para saque.')
        elif valor > 500:
            print('Limite de saque diário é de R$ 500,00.')
        elif self.num_saques >= 3:
            print('Limite diário de 3 saques atingido.')
        elif valor > self.saldo:
            print('Saldo insuficiente para realizar o saque.')
        else:
            self.saques.append(valor)
            self.saldo -= valor
            self.num_saques += 1
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
    
    def extrato(self):
        print('Extrato:')
        if not self.depositos and not self.saques:
            print('Não foram realizadas movimentações.')
        else:
            for deposito in self.depositos:
                print(f'Depósito: R$ {deposito:.2f}')
            for saque in self.saques:
                print(f'Saque: R$ {saque:.2f}')
            print(f'Saldo atual: R$ {self.saldo:.2f}')