# TPC2 - Análise de um dataset de obras musicais

## Autor
- Diogo Rafael dos Santos Barros
- A100600

## Resumo
Neste TPC, foi proibido de se usar o módulo **CSV** do Python. Tem de ser possível ler o dataset, processá-lo e criar os seguintes resultados:
- Lista **ordenada alfabeticamente** dos compositores musicais;
- Distribuição das obras por período: quantas **obras catalogadas em cada período**;
- Dicionário em que a cada período está a associada uma **lista alfabética dos títulos das obras desse período.**

---

## Estrutura do Projeto
```
├── data/
│   ├── obras.csv          # Arquivo CSV original
│   ├── obras_novo.csv     # Arquivo CSV limpo
├── results/
│   ├── compositores.txt   # Lista ordenada de compositores
│   ├── obras_por_periodo.txt # Contagem de obras por período
│   ├── titulos_por_periodo.txt # Lista de obras por período
├── tpc2.py              # Código principal
├── README.md              # Documentação
```
---

## Funcionamento
1. **Tratamento e Limpeza de Dados**
   - Reconstroi as entradas com quebras de linhas do CSV original.
   - Remove a coluna "desc" (descrição das obras).
   - Cria e guarda um novo arquivo `obras_novo.csv` com os dados limpos.

2. **Extração de Informações**
   - Lista e ordena alfabeticamente os compositores únicos.
   - Conta quantas obras pertencem a cada período musical.
   - Organiza um dicionário de títulos das obras, agrupados por período.

3. **Armazenamento de Resultados**
   - Guarda os dados processados nos seguintes arquivos:
     - `compositores.txt` → Lista ordenada de compositores.
     - `obras_por_periodo.txt` → Quantidade de obras por período musical.
     - `titulos_por_periodo.txt` → Lista de títulos organizados por período.
