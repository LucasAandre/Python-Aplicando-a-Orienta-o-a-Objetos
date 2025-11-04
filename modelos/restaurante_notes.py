from modelos.avaliacao import Avaliacao

class Restaurante: # Uma classe chamada Restaurante | Nome de classe sempre com a primeira letra maiúscula, por convenção
    '''Atributos da classe:'''
    restaurantes = []
    def __init__(self, nome, categoria): # O self serve para não confundirmos os atributos ao criar diversos objetos
        '''O __init__ sempre será executado quando um objeto for criado'''
        self._nome = nome.title() # O self.nome será o nome do objeto que será criado | title(): Define todas as primeiras letras como maiúsculas
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self) # Assim que criado, o objeto (restaurante) será adicionado na lista de restaurantes
    
    def __str__(self):
        '''Representação em texto'''
        return f'{self._nome} | {self._categoria}' # Retorna como texto para o objeto que eu chamar (Exibe isso ao invés do endereço da memória)
    
    @classmethod
    def listar_restaurantes(cls): # Um método para a classe e não para os objetos
        print(f'{'RESTAURANTE'.ljust(25)} | {'CATEGORIA'.ljust(25)} | {'STATUS'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}') # Não uso self, pois já declarei que estou puxando da lista de restaurantes. Logo, é DAQUELE restaurante em específico, vide o for

    @property # Responsável por alterar a forma como determinado atributo é lido
    def ativo(self):
        '''Método responsável por alterar a forma como o status será lido'''
        return '✅' if self._ativo else '✘' # Se ativo, se não ativo
    
    def alternar_status(self): # Um método criado para cada instância / objeto
        self._ativo = not self._ativo # Estou invertendo o status do meu objeto

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

'''self representa a própria instância (ou seja, o objeto que está sendo criado)'''

'''
O Python adota como padrão "self", porém pode ser QUALQUER palavra.
'''

'''
__init__ / __str__ : Métodos especiais
'''

restaurante_bella_sushi = Restaurante('Bella Sushi', 'Japonesa') # Uma instância da minha classe Restaurante, ou seja, um objeto
restaurante_di_napoli = Restaurante('Di Napoli', 'Italiana') # Uma instância da minha classe Restaurante, ou seja, um objeto

'''
As variáveis restaurante_bella_sushi e restaurante_di_napoli são objetos (instâncias) da classe Restaurante.
Você instanciou a classe duas vezes.
'''

print(restaurante_bella_sushi) # Exibição sem o __str__: <__main__.Restaurante object at 0x7384d4338230>
print()

print(vars(restaurante_bella_sushi)) # {'nome': 'Bella Sushi', 'categoria': 'Japonesa', 'ativo': False}
print()

print(f'{restaurante_bella_sushi} e {restaurante_di_napoli}') # Bella Sushi | Japonesa e Di Napoli | Italiana
print()

print(restaurante_di_napoli._nome) # Di Napoli
print()

# Exibição dos métodos especiais que posso utilizar:
print(dir(restaurante_di_napoli))
'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', 
'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
'__weakref__', 'ativo', 'categoria', 'nome']
'''
print()

Restaurante.listar_restaurantes() # Método da classe: classmethod
'''
RESTAURANTE               | CATEGORIA                 | STATUS
Bella Sushi               | Japonesa                  | ✘
Di Napoli                 | Italiana                  | ✘
'''
print()

print(restaurante_bella_sushi.ativo) # ✘
print()

restaurante_bella_sushi.alternar_status() # Dessa forma, estou alterando o status antes da exibição da lista | Método criado para os objetos
Restaurante.listar_restaurantes()
'''
RESTAURANTE               | CATEGORIA                 | STATUS
Bella Sushi               | Japonesa                  | ✅
Di Napoli                 | Italiana                  | ✘
'''
print()
