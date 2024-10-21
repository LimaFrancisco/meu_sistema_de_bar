from models.atendente import Atendente
from models.pedido import Pedido
from models.produto import Produto

atendente = Atendente('Isac', 123)

produto1 = Produto('Cerveja', 1 , 7.00)
produto2 = Produto('Cachaça', 2, 4.00)
produto3 = Produto('Conhaque', 3, 3.00)
produto4 = Produto('Refrigerante', 4, 5.00)

produtos = [produto1, produto1, produto1, produto2, produto3, produto2, produto4]

pedido = Pedido(1, atendente, produtos)
dados = pedido.exibir_dados_pedido()

print(dados)