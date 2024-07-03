"""
This script displays a menu of options for managing restaurants.
"""
import os

restaurantes = [
    {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
    {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
    {'nome': 'Cantina', 'categoria': 'Italiana', 'ativo': False}
]


def exibir_nome_do_programa():
    """
    This function displays the name of the program.
    """
    print(
        """
███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗  ███████╗██╗░░░░░░█████╗░██╗░░░██╗░█████╗░██████╗░
██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝  ██╔════╝██║░░░░░██╔══██╗██║░░░██║██╔══██╗██╔══██╗
█████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░  █████╗░░██║░░░░░███████║╚██╗░██╔╝██║░░██║██████╔╝
██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗  ██╔══╝░░██║░░░░░██╔══██║░╚████╔╝░██║░░██║██╔══██╗
███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝  ██║░░░░░███████╗██║░░██║░░╚██╔╝░░╚█████╔╝██║░░██║
╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  ╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
        """
    )


def exibir_opcoes():
    """
    Exibe as opções disponíveis para o usuário.
    """
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')


def finalizar_app():
    """
    Finalizes the app by displaying a subtitle.
    """
    exibir_subtitulo('Finalizar app')


def voltar_ao_menu_principal():
    """
    Função que aguarda a entrada do usuário para voltar ao menu principal.
    """
    input('\nDigite uma tecla para voltar ao menu ')
    main()


def opcao_invalida():
    """
    Prints a message indicating that the option is invalid.
    """
    print('Opção inválida!\n')
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    """
    Function to display a subtitle.

    Parameters:
    texto (str): The subtitle text to be displayed.

    Returns:
    None
    """
    os.system('clear')
    line = '*' * len(texto)
    print(line)
    print(texto)
    print(line)
    print()


def cadastrar_novo_restaurante():
    """
    Função para cadastrar um novo restaurante.

    Solicita ao usuário o nome e a categoria do restaurante a ser cadastrado.
    Cria um dicionário com as informações do restaurante e adiciona-o à lista de restaurantes.
    Imprime uma mensagem de sucesso ao cadastrar o restaurante.
    Chama a função voltar_ao_menu_principal para retornar ao menu principal.
    """
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')

    restaurante = {
        'nome': nome_do_restaurante,
        'categoria': categoria_do_restaurante,
        'ativo': False
    }

    restaurantes.append(restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

    voltar_ao_menu_principal()


def listar_restaurantes():
    """
    This function lists the restaurants.

    It displays a table with the restaurant number, name, category, and state.
    The table is printed to the console.

    Parameters:
    None

    Returns:
    None

    ou pode usar ljust para alinhar
    print(f"{'Nº'.ljust(3)}")
    """

    exibir_subtitulo('Listando restaurantes')

    print(f"{'Nº':<3} | {'Nome':<20} | {'Categoria':<20} | {'Estado':<10}")
    for index, restaurante in enumerate(restaurantes):
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']

        print(f'{index + 1:<3} | {nome:<20} | {categoria:<20} | {"Ativo" if ativo else "Inativo":<10}')


def listando_restaurantes():
    """
    Lists all the restaurants.
    """
    listar_restaurantes()

    voltar_ao_menu_principal()


def alterar_estado_do_restaurante():
    """
    Altera o estado (ativo ou inativo) de um restaurante selecionado.

    Exibe uma lista de restaurantes disponíveis e solicita ao usuário que digite o número do restaurante que deseja alterar o estado.
    Em seguida, altera o estado do restaurante selecionado e exibe uma mensagem de sucesso.
    Caso o restaurante não seja encontrado, exibe uma mensagem informando que o restaurante não foi encontrado.

    """
    exibir_subtitulo('Alterando status do restaurante')

    listar_restaurantes()

    restaurante_selecionado = int(input('\nDigite o número do restaurante que deseja alterar o estado: ')) - 1
    restaurante_encontrado = False

    for index, restaurante in enumerate(restaurantes):
        if restaurante_selecionado == index:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {restaurante["nome"]} foi desativado com sucesso!' \
                if not restaurante['ativo'] else f'O restaurante {restaurante["nome"]} foi ativado com sucesso!'
            print(mensagem)

    if not restaurante_encontrado:
        print('Restaurante não encontrado!')

    voltar_ao_menu_principal()


def escolher_opcao():
    """
    Função responsável por solicitar ao usuário que escolha uma opção e executar a ação correspondente.

    Raises:
        RuntimeError: Se ocorrer algum erro ao escolher a opção.

    """
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listando_restaurantes()
        elif opcao_escolhida == 3:
            alterar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except Exception as e:
        raise RuntimeError("Erro ao escolher opção: ", e) from e


def main():
    """
    This is the main function of the program.
    It clears the screen, displays the program name,
    shows the available options, and allows the user
    to choose an option.
    """
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
