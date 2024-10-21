from .atendente import Atendente
from .produto import Produto
from typing import Type, List

class Pedido:
    def __init__(self, id_pedido: Type[int], responsavel: Type[Atendente], produtos: Type[List[Produto]]) -> Type[None]:
        self.__id_pedido = id_pedido
        self.__responsavel = responsavel
        self.__produtos = produtos

    def adicionar_produto(self, novo_produto: Type[Produto]) -> Type[None]:
        self.__produtos.append(novo_produto)

    def remover_produto(self, id_produto: Type[int], quantidade: Type[int]) -> Type[None]:
        for item in self.__produtos:
            if item.exibir_id_produto() == id_produto:
                self.__produtos.remove(item)
                quantidade -= 1

                if quantidade == 0:
                    break
    
    def exibir_dados_pedido(self) -> Type[str]:
        dados = f'ID DO PEDIDO: {self.__id_pedido}\n'
        dados += f'{'-' * 51}\n'

        dados += '----------------- ITENS DO PEDIDO -----------------\n'

        for produto in self.__produtos:
            if produto.exibir_nome_produto() not in dados:
                quantidade = self.__produtos.count(produto)
                dados += f'{produto.exibir_nome_produto() + ' ':-<39} {quantidade}X R$ {produto.exibir_preco() * quantidade:.2f}\n'

        dados += f'{'-' * 51}\n'
        dados += f'RESPONSAVEL PELO PEDIDO: {self.__responsavel.exibir_nome_atendente()}'
            

        return dados
