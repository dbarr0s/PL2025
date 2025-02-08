# TPC1 - Somador On/Off
Pretende-se um programa que some todas as sequências de dígitos que encontre num texto;

## Autor
- Diogo Rafael dos Santos Barros
- A100600

## Resumo:
- Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
- Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
- Sempre que encontrar o caráter “=”, o resultado da soma é colocado na saída.
- Sempre que encontrar um "=", retorna o valor calculado até aquele momento e no fim do ciclo, retorna o resultado da última soma efetuada (total somado).

## Funcionamento:
- O código começa por ler um arquivo que contém comandos **(on, off, =)** e **números.**
- Enquanto o comando **'On'** estiver ativo, através da variável **'ligado'**, os números vão sendo somados.
- Quando o comando **'='** aparece, a soma parcial é **exibida.**
- Quando o comando **'off'** aparece, pausa a soma até que um novo **'On'** apareça.
- No final do percurso de todo o txt, o programa imprime o **resultado final da soma.**