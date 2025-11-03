import os

restaurantes = [{'nome': 'Bella Sushi', 'categoria': 'Japonesa', 'ativo': False}, 
                {'nome': 'Don Corleone', 'categoria': 'Italiana', 'ativo': True},
                {'nome': 'Ponto Nordestino', 'categoria': 'Nordestina', 'ativo': False}]

def exibir_nome_programa():
    '''Exibe o nome estilizado da aplicação'''
    print('''
        
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    ''')

    print()


def exibir_opcoes():
    '''Essa função é responsável por exibir o menu de opções'''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Alterar Status do Restaurante')
    print('4. Sair\n')


def finalizar_app():
    '''Essa função é responsável por finalizar a aplicação
    
    Outputs:
    - Finaliza a aplicação
    '''
    os.system('clear')
    print('Finalizando o programa\n')


def escolher_opcao():
    '''Essa função é responsável por validar a escolha do usuário
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''
    try:
        opcao_escolhida = int(input('\nEscolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_restaurantes()

        elif opcao_escolhida == 2:
            listar_restaurantes()

        elif opcao_escolhida == 3:
            alterar_status()
        
        elif opcao_escolhida == 4:
            finalizar_app()

        else:
            opcao_invalida()
    
    except:
        opcao_invalida()
    
    '''
    Existe a opção math (Switch Case do C++):

    opcao_escolhida = int(input('Escolha uma opção: '))

    match opcao_escolhida:
    
    case 1:
        print('Adicionar restaurante')
    case 2:
        print('Listar restaurantes')
    case 3:
        print('Ativar restaurante')
    case 4:
        print('Finalizar app')
    case _:
        print('Opção inválida!')
    '''


def opcao_invalida():
    '''Essa função é a responsável por apresentar o erro em caso de uma opção inválida
    
    Outputs:
    - Retorna ao menu principal
    '''
    print('\nOpção inválida! Digite apenas números de 1 a 4.\n')
    voltar_menu_principal()


def cadastrar_restaurantes():
    '''Essa função é a responsável por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria do restaurante

    Outputs:
    - Adiciona um novo restaurante à lista de restaurantes
    '''
    titulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_restaurante = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria_restaurante, 'ativo': False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    voltar_menu_principal()


def listar_restaurantes():
    '''Essa função é a responsável por listar os restaurantes cadastrados
    
    Outputs:
    - Exibe a lista de restaurantes na tela
    '''
    titulo('Lista de Restaurantes')
    
    print(f'{'RESTAURANTE'.ljust(23)} | {'CATEGORIA'.ljust(20)} | {'STATUS'}')
    for i, restaurante in enumerate(restaurantes, start=1):
        status = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'{i}. {restaurante['nome'].ljust(20)} | {restaurante['categoria'].ljust(20)} | {status}')

    voltar_menu_principal()


def voltar_menu_principal():
    '''Essa função é a responsável por voltar ao menu principal
    
    Outputs:
    - Retorna ao menu principal após o usuário teclar algo
    '''
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()


def titulo(string):
    '''Essa função é a responsável por apresentar o título de cada outra função'''
    os.system('clear')
    linha = '*' * (len(string))
    print(linha)
    print(string)
    print(linha)
    print()


def alterar_status():
    '''Essa função é a responsável por alterar o status do restaurante
    
    Inputs:
    - Nome do restaurante
    - Escolha do usuário (sim ou não)

    Outputs:
    - Status da ativação (via mensagem)
    '''
    titulo('Alterando status do Restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o status: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante.upper() == restaurante['nome'].upper():
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo'] # altera (inverte) o status do restaurante
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restautante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante ainda não está cadastrado em nossa base de dados.\n')
        escolha = input('Deseja cadastrar o restaurante? [S/N]: ').upper()

        if 'S' in escolha:
            cadastrar_restaurantes()
            
    voltar_menu_principal()

def main():
    '''Essa função é a responsável pelo menu principal da aplicação'''
    os.system('clear')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()

'''
A variável __name__ não é sempre igual a '__main__', mas ela assume esse valor em situações específicas.

Em resumo:

__name__ == '__main__': Isso acontece quando o arquivo Python é executado diretamente. Ou seja, você roda 
o script usando python nome_do_arquivo.py. Nesse caso, o Python define a variável __name__ como '__main__'.
__name__ == 'nome_do_módulo': Quando um arquivo Python é importado como um módulo em outro arquivo, a 
variável __name__ recebe o nome do módulo (que geralmente é o nome do arquivo sem a extensão .py).
Analogia:

Imagine que você tem uma receita de bolo (arquivo_receita.py).

Executando diretamente: Se você decidir fazer o bolo seguindo essa receita diretamente (python arquivo_receita.py), 
então, para a receita, ela é a "principal" (__main__).
Importando a receita: Se você tem um livro de receitas (meu_livro_de_receitas.py) e usa um trecho da receita do bolo
 (import arquivo_receita), então a receita do bolo é apenas um "módulo" dentro do seu livro, e o nome dela é arquivo_receita.
No contexto da aula, a condição if __name__ == '__main__': é usada para garantir que a função main() seja executada
 apenas quando o script é o programa principal, e não quando é importado como um módulo em outro lugar.
'''
