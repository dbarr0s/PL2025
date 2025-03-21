from analisador_sint import parse_input

while True:
    linha = input("Introduza uma expressão (ou 'sair' para terminar): ")
    
    if not linha:  # Se a entrada estiver vazia, ignora e continua o loop
        continue

    if linha.lower() == "sair":
        print("Encerrando o programa...")
        break

    res = parse_input(linha)

    if res is not None:
        print(f"\nExpressão: {linha}")
        print(f"\nResultado = {res}")
    else:
        print("Erro ao avaliar a expressão. Tente novamente.")