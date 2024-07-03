from models.avaliacao import Avaliacao


class Restaurante:
    restaurantes = []

    def __init__(self, nome: str, categoria: str):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'Nome: {self._nome}, Categoria: {self._categoria}, Ativo: {self._ativo}'

    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nº':<3} | {'Nome':<20} | {'Categoria':<20} | {'Avaliação':<20} | {'Estado':<10}")
        for index, restaurante in enumerate(cls.restaurantes):
            nome = restaurante._nome
            categoria = restaurante._categoria
            ativo = restaurante.ativo
            media = restaurante.media_avaliacao

            print(f'{index + 1:<3} | {nome:<20} | {categoria:<20} | {media:<20} | {ativo:<10}')

    @property
    def ativo(self):
        return '✅' if self._ativo else '❌'

    def alterar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 > nota >= 5:
            raise ValueError('Nota inválida. A nota deve ser entre 0 e 5.')
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self) -> (str | float):
        if not self._avaliacao:
            return '-'

        soma_notas = sum([avaliacao._nota for avaliacao in self._avaliacao])
        qtd_notas = len(self._avaliacao)
        media = round(soma_notas / qtd_notas, 1)

        return media
