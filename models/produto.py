from typing import Type 

class Produto:
    def __init__(self, nome_produto: Type[str], id_produto: Type[int], preco: Type[float]) -> Type[None]:
        self.__nome_produto = nome_produto
        self.__id_produto = id_produto
        self.__preco = preco

    def exibir_nome_produto(self) -> Type[str]:
        return self.__nome_produto

    def exibir_id_produto(self) -> Type[int]:
        return self.__id_produto

    def exibir_preco(self) -> Type[float]:
        return self.__preco

    def atualizar_preco(self, novo_preco: Type[float]) -> Type[None]:
        self.__preco = novo_preco
        