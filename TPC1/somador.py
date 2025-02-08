import re

def somador(arquivo):
    soma = 0
    ligado = False

    with open(arquivo, 'r') as file:
        texto = file.read()

        # Ajuste da expressão regular para capturar números inteiros positivos e negativos
        lista = re.findall(r'(off|on|=|-?\d+)', texto, flags=re.IGNORECASE)
        #print(lista)
        
        for element in lista:
            if element.lower() == 'on':
                ligado = True
            elif element.lower() == 'off':
                ligado = False
            elif element == '=':
                print(f'Resultado do momento = {soma}')
            else:
                num = int(element)
                if ligado:
                    soma += num
                    
    return soma

def main():
    resultado_final = somador("somador.txt")
    #resultado_final = somador("somador1.txt")
    print(f'Resultado Final = {resultado_final}')

if __name__ == '__main__':
    main()