import json
import re
import ply.lex as lex
from tabulate import tabulate

tokens = (
    'LISTAR', 
    'SAIR', 
    'SALDO', 
    'MOEDA', 
    'SELECIONAR', 
    'ADICIONAR'
    )

def t_MOEDA(t):
    r'MOEDA\s+((\d+e|\d+c)(,\s*(\d+e|\d+c))*)'
    valores = re.findall(r'(\d+e|\d+c)', t.value)
    for valor in valores:
        if valor[-1] == 'e':
            t.lexer.saldo += int(valor[:-1])
        else:
            t.lexer.saldo += int(valor[:-1]) / 100
    return t

def t_LISTAR(t):
    r'LISTAR'
    print("Lista de produtos:")
    headers = ["COD", "NOME", "QUANTIDADE", "PREÇO"]
    table = []
    for produto in t.lexer.data:
        table.append([produto['cod'], produto['nome'], produto['quant'], f"{produto['preco']}€"])
    print(tabulate(table, headers, tablefmt="grid"))
    return t

def t_ADICIONAR(t):
    r'ADICIONAR\s+\w+\s+\d+\s+\d+(\.\d+)?'
    input_parts = t.value.split()
    produto_cod = input_parts[1]
    quantidade = int(input_parts[2])
    preco = float(input_parts[3])
    
    produto = next((p for p in t.lexer.data if p['cod'] == produto_cod), None)
    if produto:
        produto['quant'] += quantidade
        produto['preco'] = preco
    else:
        nome_produto = input("Nome do novo produto: ")
        novo_produto = {
            'cod': produto_cod,
            'nome': nome_produto,
            'quant': quantidade,
            'preco': preco
        }
        t.lexer.data.append(novo_produto)
    print(f"{quantidade} unidades de {produto_cod} adicionadas ao estoque.")
    
    with open("./stock.json", "w") as file:
        json.dump(t.lexer.data, file, indent=4)
    return t

def t_SALDO(t):
    r'SALDO'
    print(f"Saldo disponível: {t.lexer.saldo}€")
    return t

def t_SELECIONAR(t):
    r'SELECIONAR\s+\w+'
    produto_cod = t.value.split()[1]
    produto = next((p for p in t.lexer.data if p['cod'] == produto_cod), None)
    if produto:
        if t.lexer.saldo >= produto['preco']:
            if produto['quant'] > 0:
                t.lexer.saldo -= produto['preco']
                produto['quant'] -= 1
                print(f"Compra efetuada com sucesso: {produto['nome']}")
            else:
                print(f"Produto {produto_cod} esgotado.")
        else:
            print(f"Saldo insuficiente para comprar: {produto['nome']}")
    else:
        print(f"Produto inexistente com código: {produto_cod}")
        
    with open("./stock.json", "w") as file:
        json.dump(t.lexer.data, file, indent=4)
    return t

def t_SAIR(t):
    r'SAIR'
    if t.lexer.saldo > 0:
        print(f"Retire o seu troco: {t.lexer.saldo}€")
        t.lexer.flag = True
    else:
        print("Obrigado pela preferência.")
        t.lexer.flag = True
    return t

def t_error(t):
    print("Comando inválido.")
    t.lexer.skip(1)
    
t_ignore = ' \t\n'

def main():
    lexer = lex.lex()
    
    with open("./stock.json", "r") as file:
        data = json.load(file)

    lexer.data = data
    lexer.flag = False
    lexer.saldo = 0

    # Display initial message
    print("Bem-vindo à máquina de venda automática.")
    print("Comandos disponíveis:")
    print("-> LISTAR")
    print("-> SALDO")
    print("-> MOEDA <VALOR>")
    print("-> SELECIONAR <COD>")
    print("-> ADICIONAR <COD> <QUANT> <PREÇO>")
    print("-> SAIR")

    # Main loop
    while not lexer.flag:
        input_user = input("Operação a realizar: ")
        lexer.input(input_user)
        token = lexer.token()
        if not token:
            print("Comando inválido.")

if __name__ == "__main__":
    main()