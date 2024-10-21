from typing import Type

class Atendente:
    def __init__(self, nome_atendente: Type[str], id_atendente: Type[int]) -> Type[None]:
        self.__nome_atendente = nome_atendente
        self.__id_atendente = id_atendente

    def exibir_nome_atendente(self) -> Type[str]:
        return self.__nome_atendente
    
    def exibir_id_atendente(self) -> Type[int]:
        return self.__id_atendente
    