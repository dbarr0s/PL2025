# TPC4 - Analisador Léxico para Consultas SPARQL

## Autor
- Diogo Rafael dos Santos Barros
- A100600

## Resumo
Neste TPC, foi construído um **analisador léxico** para uma linguagem de consulta inspirada no **SPARQL**, que permite escrever queries como:

```
# DBPedia: obras de Chuck Berry
SELECT ?nome ?desc WHERE {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000
```

## Estrutura do Projeto
```
├── lex.py                 # Código principal
├── README.md              # Documentação
```

## Funcionamento
1. **Definição dos Tokens**
   - O **analisador léxico** reconhece os principais componentes da linguagem:
     - **Palavras-chave**: `SELECT`, `WHERE`, `LIMIT`
     - **Variáveis**: `?s`, `?nome`, `?desc`
     - **Prefixos RDF**: `dbo:MusicalArtist`, `foaf:name`
     - **Strings com idioma**: `"Chuck Berry"@en`
     - **Símbolos de estrutura**: `{ } .`
     - **Comentários**: `# ...`

2. **Processamento de uma Query**
   - Lê uma **consulta SPARQL**.
   - Identifica os **tokens** e classifica-os corretamente.
   - Exibe a lista de tokens gerados no terminal.
   - Exemplo de saída:
   

   ```
    LexToken(COMMAND,'select',4,34)
    LexToken(VARS,'?nome',4,41)
    LexToken(VARS,'?desc',4,47)
    LexToken(WHERE,'where',4,53)
    LexToken({,'{',4,59)
    LexToken(VARS,'?s',5,65)
    LexToken(RDF_TYPE,'a',5,68)
    LexToken(PREFIX,'dbo:MusicalArtist',5,70)
    LexToken(.,'.',5,87)
    LexToken(VARS,'?s',6,93)
   ...
   ```
