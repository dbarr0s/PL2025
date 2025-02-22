# TPC3 - Conversor de Markdown para HTML

## Autor
- Diogo Rafael dos Santos Barros
- A100600

## Resumo
Este projeto consiste num conversor de **Markdown para HTML**, capaz de transformar elementos **básicos de formatação** nos seus equivalentes do **HTML.**

## Estrutura do Projeto
```
├── md/
│   ├── exemplo.md          # Arquivo Markdown de entrada
├── html/
│   ├── exemplo.html        # Arquivo HTML criado
├── conversor.py            # Código principal
├── README.md               # Documentação
```

## Funcionamento
O script `conversor.py` lê um arquivo Markdown e converte os seus elementos principais para HTML. Os seguintes elementos são suportados:

### 1. Cabeçalhos
Linhas iniciadas com `#`, `##` ou `###` são convertidas para `<h1>`, `<h2>` e `<h3>`, respectivamente.

**Entrada:**
```
# Título Principal
## Subtítulo
### Cabeçalho menor
```

**Saída:**
```html
<h1>Título Principal</h1>
<h2>Subtítulo</h2>
<h3>Cabeçalho menor</h3>
```

### 2. Bold
Pedaços de texto entre `**` são convertidos para `<b>`.

**Entrada:** `Este é um **exemplo** de bold.`

**Saída:** `Este é um <b>exemplo</b> de bold.`

### 3. Itálico
Pedaços de texto entre `*` são convertidos para `<i>`.

**Entrada:** `Este é um *exemplo* de itálico.`

**Saída:** `Este é um <i>exemplo</i> de itálico.`

### 4. Listas Ordenadas
Linhas numeradas são convertidas em listas ordenadas `<ol>`.

**Entrada:**
```
1. Primeiro item
2. Segundo item
3. Terceiro item
```

**Saída:**
```html
<ol>
<li>Primeiro item</li>
<li>Segundo item</li>
<li>Terceiro item</li>
</ol>
```

### 5. Links
Links escritos no formato `[texto](URL)` são convertidos para `<a>`.

**Entrada:** `Como pode ser consultado em [página da UC](http://www.uc.pt)`

**Saída:** `Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>`

### 6. Imagens
Imagens escritas no formato `![alt](URL)` são convertidas para `<img>`.

**Entrada:** `Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com)`

**Saída:** `Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/>`
