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
        print(f'{'RESTAURANTE'.ljust(25)} | {'CATEGORIA'.ljust(25)} | {'AVALIAÇÃO'.ljust(25)} | {'STATUS'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}') # Não uso self, pois já declarei que estou puxando da lista de restaurantes. Logo, é DAQUELE restaurante em específico, vide o for

    @property # Responsável por alterar a forma como determinado atributo é lido
    def ativo(self):
        '''Método responsável por alterar a forma como o status será lido'''
        return '✅' if self._ativo else '✘' # Se ativo, se não ativo
    
    def alternar_status(self): # Um método criado para cada instância / objeto
        self._ativo = not self._ativo # Estou invertendo o status do meu objeto

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 'Sem avaliações'
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_notas / quantidade_notas, 1)
        return media
