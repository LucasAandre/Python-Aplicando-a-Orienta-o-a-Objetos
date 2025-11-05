'''
1. Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. 
Inicie um atributo chamado disponivel como True por padrão.

2. Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor 
e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.

3. Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. 
Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.

4. Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e 
retorna uma lista dos livros disponíveis publicados nesse ano.
'''
from modelos.livro import Livro

def main():
    # 2
    livro1 = []
    titulo1 = input('Digite o título do primeiro livro: ')
    autor1 = input('Digite o nome do autor: ')
    ano_publicacao1 = int(input('Digite o ano de lançamento do livro: '))
    livro1.append(titulo1)
    livro1.append(autor1)
    livro1.append(ano_publicacao1)
    print()

    livro2 = []
    titulo2 = input('Digite o título do segundo livro: ')
    autor2 = input('Digite o nome do autor: ')
    ano_publicacao2 = int(input('Digite o ano de lançamento do livro: '))
    livro2.append(titulo2)
    livro2.append(autor2)
    livro2.append(ano_publicacao2)
    print()

    livro3 = []
    titulo3 = input('Digite o título do terceiro livro: ')
    autor3 = input('Digite o nome do autor: ')
    ano_publicacao3 = int(input('Digite o ano de lançamento do livro: '))
    livro3.append(titulo3)
    livro3.append(autor3)
    livro3.append(ano_publicacao3)
    print()

    first_book = Livro(*livro1) # Para desempacotar os dados e ler um a um e não como lista (o que daria um erro)
    second_book = Livro(*livro2) # Para desempacotar os dados e ler um a um e não como lista (o que daria um erro)
    third_book = Livro(*livro3) # Para desempacotar os dados e ler um a um e não como lista (o que daria um erro)
    #livro2 = Livro('A Droga da Obediência', 'Pedro Bandeira', 1984)

    print(f'1. {first_book}')
    print(f'2. {second_book}')
    print(f'3. {third_book}')
    print()


    #3
    emprestimo = int(input('Digite o número do livro que deseja emprestar: '))
    
    if emprestimo == 1:
        first_book.emprestar()
    
    elif emprestimo == 2:
        second_book.emprestar()
    
    elif emprestimo == 3:
        third_book.emprestar()

    else:
        print('Opção inexistente!')
    
    Livro.listar_livros()


    #4
    print()
    ano_disponibilidade = int(input('Digite o ano de lançamento para checarmos nossa disponibilidade de livros: '))
    
    Livro.verificar_disponibilidade(ano_disponibilidade)

if __name__ == '__main__':
    main()
