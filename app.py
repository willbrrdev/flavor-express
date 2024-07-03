from models.restaurante import Restaurante

pizzaria_joao = Restaurante('Pizzaria do João', 'Pizzaria')
sorveteria_maju = Restaurante('Sorveteria da Maju', 'Sorveteria')
pastel_maju = Restaurante('Pastel da Maju', 'Pastelaria')

pizzaria_joao.alterar_estado()
pizzaria_joao.receber_avaliacao('João', 5)
pizzaria_joao.receber_avaliacao('Maria', 4)
pizzaria_joao.receber_avaliacao('José', 3)

sorveteria_maju.receber_avaliacao('João', 5)
sorveteria_maju.receber_avaliacao('Maria', 4)
sorveteria_maju.receber_avaliacao('José', 5)

pastel_maju.receber_avaliacao('João', 4)
pastel_maju.receber_avaliacao('Maria', 3)


def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()
