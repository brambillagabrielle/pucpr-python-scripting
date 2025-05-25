"""
1. Restaurante Boca Feliz
Você foi contratado pelo restaurante Boca Feliz para participar do desenvolvimento de
um pequeno controle de estoque de ingredientes iniciado em Python 3.8. O sistema já
possui desenvolvido um dicionário chamado estoque, no qual consta a lista de
ingredientes com suas respectivas quantidades. Também possui outro dicionário
chamado cardapio, no qual constam todos os ingredientes que compõe cada produto
servido no restaurante. Tais estruturas são mostradas a seguir:
estoque = {'pao': 10, 'hamburguer': 12, 'tomate': 5, 'bacon': 5, 'ovo': 5}
cardapio = {
'x-burguer': ['pao', 'hamburguer'],
'x-salada': ['pao', 'hamburguer', 'tomate'],
'x-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
'x-egg': ['pao', 'hamburguer', 'ovo'],
'x-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']
}
Sua primeira tarefa de programador consiste em desenvolver as seguintes
funcionalidades do sistema:
- Imprimir o cardápio do restaurante com as opções de produtos ofertados;
- Logo abaixo do cardápio, exibir a mensagem “O que deseja pedir (0 para sair)?”;
- Digitando “0” deve sair do programa;
- Digitando o nome do produto pode ter uma das seguintes possibilidades:
- Se o item não consta no cardápio exibir a mensagem “Item não localizado no
cardápio”;
- Se não tiver os ingredientes para o preparo do produto em estoque mostrar uma
mensagem para cada ingrediente faltante “Infelizmente acabou o {ingrediente}”;
- Se for possível produzir o produto, reduzir as quantidades de estoque e mostrar a
mensagem “um {produto} saindo no capricho!!!”;
- O programa deve continuar fazendo os pedidos até que o usuário decida sair do
mesmo.
O restaurante Boca Feliz conta com você!!!
"""

estoque = {
    'pao': 10, 
    'hamburguer': 12, 
    'tomate': 5, 
    'bacon': 5, 
    'ovo': 5
}

cardapio = {
    'x-burguer': ['pao', 'hamburguer'],
    'x-salada': ['pao', 'hamburguer', 'tomate'],
    'x-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
    'x-egg': ['pao', 'hamburguer', 'ovo'],
    'x-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']
}

for produto in cardapio:
    print("================================")
    print(f"Produto: {produto}")
    print(f"Ingredientes: {cardapio[produto]}\n")

while True:
    pedido = input("\nDigite o que deseja pedir (0 para sair): ")

    pedido_ok = True

    if pedido == 0:
        break
    elif pedido in cardapio.keys():
        for ingrediente in cardapio[pedido]:
            if estoque[ingrediente] <= 0:
                pedido_ok = False
                print(f"Infelizmente acabou o {ingrediente} :(")
            else:
                estoque[ingrediente] -= 1

        if pedido_ok:
            print(f"Um {produto} saindo no capricho!!!")
    else:
        print("Item não localizado no cardápio!")