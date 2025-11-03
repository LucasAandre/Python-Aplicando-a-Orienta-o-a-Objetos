'''
Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.

Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias 
da classe e imprima essas instâncias.

Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o 
método de classe e imprima o valor de ativo.

Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.

Crie uma instância da classe e imprima o valor da propriedade titular.
'''
class ContaBancaria:
    def __init__(self, titular='', saldo=0):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
    
    def __str__(self):
        return f'Titular da conta: {self._titular}\nSaldo da conta: R${self._saldo}\nStatus da conta: {self._ativo}\n'
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = not conta._ativo
    
    @property
    def titular(self):
        return f'Titular da conta: {self._titular}'
    
pessoa1 = ContaBancaria('Lucas')
pessoa2 = ContaBancaria('Pamela', 100000)
pessoa3 = ContaBancaria(titular='Neymar', saldo=1200.89)

print('Informações dos Usuários:\n')
print(pessoa1)
print(pessoa2)
print(pessoa3)

print(pessoa1.titular)
print(pessoa2.titular)
print(pessoa3.titular)

print()

ContaBancaria.ativar_conta(pessoa2)

print('Informações dos Usuários:\n')
print(pessoa1)
print(pessoa2)
print(pessoa3)
