from time import sleep
class Livro:
    livros = []
    consulta_livros = []
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo.title()
        self._autor = autor.title()
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f'O título {self._titulo} foi lançado pelo escritor {self._autor} em {self._ano_publicacao}'
    
    def emprestar(self):
        self._disponivel = not self._disponivel
    
    @classmethod
    def listar_livros(cls):
        print()
        print(f'{'LIVRO'.ljust(35)} | {'AUTOR'.ljust(35)} | {'ANO'.ljust(35)} | {'SITUAÇÃO'.ljust(35)}\n')
        for livro in cls.livros:
            print(f'{livro._titulo.ljust(35)} | {livro._autor.ljust(35)} | {str(livro._ano_publicacao).ljust(35)} | {livro.disponivel}')
    
    @classmethod
    def verificar_disponibilidade(cls, ano_consulta):
        print()
        print('Checando disponibilidade...\n')
        sleep(5)
        for livro in cls.livros:
            if livro._ano_publicacao == ano_consulta:
                Livro.consulta_livros.append(livro._titulo)
        
        if len(Livro.consulta_livros) >= 1:
            print(f'Temos os seguintes livros que foram publicados em {ano_consulta}:')
            for i, titulo in enumerate(Livro.consulta_livros, start=1):
                print(f'{i}. {titulo}')
        else:
            print('Não há livros disponíveis.')

    @property
    def disponivel(self):
        return f'Disponível para empréstimo' if self._disponivel else 'Não disponível para empréstimo'
    