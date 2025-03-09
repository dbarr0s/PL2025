# TPC5 - Máquina de Vending  

## Autor  
- Diogo Rafael dos Santos Barros  
- A100600  

## Resumo  
Neste TPC, foi desenvolvido um **simulador de máquina de vending**, onde os utilizadores podem:  
- **Listar produtos disponíveis**  
- **Inserir moedas para adicionar ao saldo**  
- **Selecionar um produto para comprar**  
- **Adicionar novos produtos ao stock**  
- **Consultar o saldo disponível**  
- **Sair e receber o troco**  

O programa utiliza **análise léxica** com **PLY (Python Lex-Yacc)** para interpretar os comandos introduzidos pelo utilizador.  

## Estrutura do Projeto  
```
├── maq_vending.py             # Código principal
├── stock.json             # Ficheiro com os produtos disponíveis
├── README.md              # Documentação
```

## Funcionamento  

### 1. Comandos Suportados  
Os seguintes comandos podem ser introduzidos pelo utilizador:  

| Comando                                | Descrição                                         |
|----------------------------------------|---------------------------------------------------|
| `LISTAR`                               | Mostra os produtos disponíveis                    |
| `MOEDA <valores>`                      | Adiciona saldo (ex: `MOEDA 1e, 50c`)              |
| `SALDO`                                | Mostra o saldo atual                              |
| `SELECIONAR <cod>`                     | Compra um produto pelo código                     |
| `ADICIONAR <cod> <quantidade> <preço>` | Adiciona um novo produto ou atualiza um existente |
| `SAIR`                                 | Termina a sessão e devolve o troco                |

### 2. Exemplo de Utilização  
```bash
Bem-vindo à máquina de venda automática.
Comandos disponíveis:
-> LISTAR
-> SALDO
-> MOEDA <VALOR>
-> SELECIONAR <COD>
-> ADICIONAR <COD> <QUANT> <PREÇO>
-> SAIR
Operação a realizar: 
```

### 3. Stock Inicial (`stock.json`)  
O ficheiro `stock.json` contém os produtos disponíveis na máquina:  
```json
[
    {"cod": "A10","nome": "agua","quant": 7,"preco": 0.7},
    {"cod": "B45","nome": "bolachas","quant": 7,"preco": 1.0},
    {"cod": "C67","nome": "lanche","quant": 4,"preco": 1.2},
    {"cod": "D89","nome": "batatas","quant": 6,"preco": 2.0},
    {"cod": "E12","nome": "chocolate","quant": 6,"preco": 3.0},
    {"cod": "F34","nome": "sumo","quant": 5,"preco": 3.0},
    {"cod": "G56","nome": "doces","quant": 4,"preco": 2.0},
    {"cod": "H45","nome": "bolo","quant": 5,"preco": 2.0}
]
```