import re

###################### TRATAMENTO E LIMPEZA DOS DADOS ######################

def parse_csv(file_path):
    processed_lines = []
    current_line = ""

    # Abrir o arquivo CSV e ler as linhas
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Expressão regular para detectar o ID no final da linha (exemplo: "O128")
    id_pattern = re.compile(r";O\d{1,3}$")

    # Processar as linhas para reconstruir entradas quebradas
    for line in lines[1:]:  # Ignorar cabeçalho na reconstrução
        line = line.strip()

        if current_line:
            current_line += " " + line  # Adicionar a linha atual à linha em construção
        else:
            current_line = line  # Iniciar a linha atual com a linha lida

        if id_pattern.search(line):  # Verifica se a linha contém um ID válido
            processed_lines.append(current_line)  # Adicionar a entrada completa
            current_line = ""  # Resetar a linha atual

    # Dividir corretamente os campos por ";"
    data = [remover_descricao(line.split(';')) for line in processed_lines]

    header = lines[0].strip().split(';')  # Cabeçalho do CSV
    dados = data[0:]  # Dados do CSV (excluindo o cabeçalho)
    
    header.remove('desc')
    
    return header, dados

def remover_descricao(dados):
    while len(dados) > 6:
        del dados[1]

    return dados
    

def salvar_csv(nome_arquivo, header, dados):
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        # Escrever o cabeçalho
        f.write(";".join(header) + "\n")

        # Escrever os dados
        for linha in dados:
            f.write(";".join(linha) + "\n")
            
###################### EXTRAÇÃO DE DADOS ######################

def listar_compositores_ordenados(dados):
    compositores = set()
    
    for linha in dados:
        compositores.add(linha[3])
    
    # Ordenar alfabeticamente as modalidades e retornar como uma lista
    compositores_ordenadas = sorted(compositores)
    return compositores_ordenadas

def contar_obras_por_periodo(header, dados):

    index_periodo = header.index("periodo")  # Identifica o índice da coluna 'periodo'
    contagem = {}

    for linha in dados:
        periodo = linha[index_periodo]  # Obtém o período da obra
        contagem[periodo] = contagem.get(periodo, 0) + 1  # Incrementa a contagem

    return contagem

def obras_por_periodo(header, dados):
    index_periodo = header.index("periodo")  # Índice da coluna 'periodo'
    index_nome = header.index("nome")  # Índice da coluna 'nome'

    periodos = {}

    for linha in dados:
        periodo = linha[index_periodo]
        nome = linha[index_nome]

        if periodo not in periodos:
            periodos[periodo] = []

        periodos[periodo].append(nome)

    # Ordenar alfabeticamente as obras em cada período
    for periodo in periodos:
        periodos[periodo].sort()

    return periodos

###################### ARMAZENAMENTO DE DADOS ######################

def salvar_resultados(compositores, obras_periodo, titulos_periodo):
    # Salvar lista de compositores ordenados
    with open("results/compositores.txt", "w", encoding="utf-8") as f:
        f.write(f"Lista de Compositores Ordenados:\n")
        f.write(f"\n")
        for compositor in compositores:
            f.write(compositor + "\n")

    # Salvar distribuição das obras por período
    with open("results/obras_por_periodo.txt", "w", encoding="utf-8") as f:
        f.write(f"Distribuição de Obras por Período:\n")
        f.write(f"\n")
        for periodo, quantidade in obras_periodo.items():
            f.write(f"{periodo}: {quantidade}\n")

    # Salvar dicionário de títulos por período
    with open("results/titulos_por_periodo.txt", "w", encoding="utf-8") as f:
        for periodo, titulos in titulos_periodo.items():
            f.write(f"{periodo}:\n")
            for titulo in titulos:
                f.write(f"  - {titulo}\n")
            f.write("\n") 

###################### MAIN ######################

def main():
    arquivo_csv = "data/obras.csv"
    novo_arquivo_csv = "data/obras_novo.csv"
    
    try:
        header, dados = parse_csv(arquivo_csv)
        salvar_csv(novo_arquivo_csv, header, dados)
        
        print(f"Arquivo '{novo_arquivo_csv}' atualizado com sucesso!")
        
        compositores = listar_compositores_ordenados(dados)
        obras_periodo = contar_obras_por_periodo(header, dados)
        titulos_periodo = obras_por_periodo(header, dados)
            
        salvar_resultados(compositores, obras_periodo, titulos_periodo)

        print("Arquivos 'compositores.txt', 'obras_por_periodo.txt' e 'titulos_por_periodo.txt' criados com sucesso!")
        
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_csv}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()