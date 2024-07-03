class Restaurante:
    restaurantes = []

    def __init__(self, nome: str, categoria: str):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'Nome: {self._nome}, Categoria: {self._categoria}, Ativo: {self._ativo}'

    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nº':<3} | {'Nome':<20} | {'Categoria':<20} | {'Estado':<10}")
        for index, restaurante in enumerate(cls.restaurantes):
            nome = restaurante._nome
            categoria = restaurante._categoria
            ativo = restaurante.ativo

            print(f'{index + 1:<3} | {nome:<20} | {categoria:<20} | {ativo:<10}')

    @property
    def ativo(self):
        return '✅' if self._ativo else '❌'

    def alterar_estado(self):
        self._ativo = not self._ativo


r = Restaurante('Pizzaria do João', 'Pizzaria')
r.alterar_estado()

r2 = Restaurante('Pizzaria do João 2', 'Pizzaria')
r.listar_restaurantes()
