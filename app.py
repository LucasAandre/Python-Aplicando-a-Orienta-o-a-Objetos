from modelos.restaurante import Restaurante # Da pasta modelos e arquivo restaurante, importe a classe Restaurante

restaurante_hamburger = Restaurante("Deivid's Burger", 'Hamburger')
restaurante_mexicano = Restaurante('Sí Señor', 'Mexicana')
restaurante_arabe = Restaurante('Habybe', 'Árabe')

restaurante_mexicano.alternar_status()

restaurante_arabe.receber_avaliacao('Lucas', 10)
restaurante_arabe.receber_avaliacao('Julia', 10)
restaurante_hamburger.receber_avaliacao('Pamela', 5.4)

def main():
    Restaurante.listar_restaurantes()
    #print(restaurante_arabe.ativo) # ✘


if __name__ == '__main__': # Se for meu arquivo principal da aplicação (main)
    main()
