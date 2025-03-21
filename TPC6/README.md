# TPC6 - Analisador Léxico, Sintático para Expressões Aritméticas

## Autor
- Diogo Rafael dos Santos Barros
- A100600

## Resumo

Este projeto consiste num **analisador léxico e sintático** para expressões aritméticas, utilizando **PLY (Python Lex-Yacc)**. O objetivo é **reconhecer e avaliar expressões matemáticas**, seguindo uma gramática LL(1).

## Estrutura do Projeto
```
├── analisador_lex.py     # Analisador Léxico 
├── analisador_sint.py    # Analisador Sintático 
├── programa.py           # Interface interativa 
├── README.md             # Documentação
```

---

## Funcionamento
### Analisador Léxico (`analisador_lex.py`)
O analisador léxico identifica os **tokens básicos** usados nas expressões:
- **Operadores**: `+`, `-`, `*`, `/`
- **Parênteses**: `(` e `)`
- **Números inteiros**

**Exemplo de tokenização:**
```
Entrada: 3 + 5 * (2 - 1)
Tokens:  [NUMBER, PLUS, NUMBER, TIMES, LPAREN, NUMBER, MINUS, NUMBER, RPAREN]
```

---

### Analisador Sintático (`analisador_sint.py`)
O analisador sintático constrói uma **árvore de derivação** e avalia a expressão com base na seguinte **gramática LL(1)**:

```
Rule 0     S' -> expression
Rule 1     expression -> expression PLUS term
Rule 2     expression -> expression MINUS term
Rule 3     expression -> term
Rule 4     term -> term TIMES factor
Rule 5     term -> term DIVIDE factor
Rule 6     term -> factor
Rule 7     factor -> NUMBER
Rule 8     factor -> LPAREN expression RPAREN
```

**Prioridades entre os operadores:**
- `*` e `/` têm **maior prioridade** que `+` e `-`.
- Os **parênteses** alteram a prioridade natural.

---

### Interface de Utilização (`programa.py`)
O programa permite ao utilizador inserir expressões matemáticas e obter os resultados de imediato. Ele:
1. Solicita uma **expressão matemática**.
2. Analisa a **sintaxe e prioridade dos operadores**.
3. Calcula e exibe o **resultado**.
4. Continua a aceitar entradas até que o utilizador digite **"sair"**.

---

## Expressões Testadas
```
-> 2+3
-> 67-(2+3*4)
-> (9-2)*(13-4)
-> (9+2-3)*(12/4)
-> (9/3-2)*(13-4)
-> 2*(3+4)
-> 14/2+3*4
-> (2*3)*(4/1)+(12/4*3)
```

---

## Exemplo de Uso
```
Introduza uma expressão (ou 'sair' para terminar): (2*3)*(4/1)+(12/4*3)

Expressão: (2*3)*(4/1)+(12/4*3)

Resultado = 33.0

Introduza uma expressão (ou 'sair' para terminar): (9/3-2)*(13-4)

Expressão: (9/3-2)*(13-4)

Resultado = 9.0

Introduza uma expressão (ou 'sair' para terminar): 14/2+3*4 

Expressão: 14/2+3*4 

Resultado = 19.0

Introduza uma expressão (ou 'sair' para terminar): sair
Encerrando o programa...
```
---